#include "read_resume_data.h"

#include <libtorrent/add_torrent_params.hpp>
#include <libtorrent/read_resume_data.hpp>

#include "add_torrent_params.h"

using lt::ReadResumeData;

NAN_MODULE_INIT(ReadResumeData::Init)
{
    Nan::Set(
        target,
        Nan::New("read_resume_data").ToLocalChecked(),
        Nan::New<v8::FunctionTemplate>(DoReadResumeData)->GetFunction());
}

NAN_METHOD(ReadResumeData::DoReadResumeData)
{
    std::string buf;

    if (info[0]->IsString())
    {
        buf = *Nan::Utf8String(info[0]);
    }
    else
    {
        buf = std::string(
            node::Buffer::Data(info[0]),
            node::Buffer::Length(info[0]));
    }

    libtorrent::error_code ec;
    libtorrent::add_torrent_params params = libtorrent::read_resume_data(
        buf.c_str(),
        static_cast<int>(buf.size()),
        ec);

    if (ec)
    {
        Nan::ThrowError(ec.message().c_str());
        return;
    }

    info.GetReturnValue().Set(AddTorrentParams::ToObject(params));
}
