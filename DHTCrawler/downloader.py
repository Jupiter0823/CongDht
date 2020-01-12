import libtorrent as lt
import time

def download():
    ses = lt.session()
    ses.listen_on(6881, 6891)
    params = {
        'save_path': '~/Downloads',
        'storage_mode': lt.storage_mode_t(2),
        'paused': False,
        'auto_managed': True,
        'duplicate_is_error': True}
    link = "magnet:?xt=urn:btih:1d70a615e3280eec79c5576f6c23fecbda8e24c3&dn=Maleficent.Mistress.Of.Evil.2019.1080p.WEBRip.x264-MP4&tr=udp%3A%2F%2Ftracker.leechers-paradise.org%3A6969&tr=udp%3A%2F%2Ftracker.openbittorrent.com%3A80&tr=udp%3A%2F%2Fopen.demonii.com%3A1337&tr=udp%3A%2F%2Ftracker.coppersurfer.tk%3A6969&tr=udp%3A%2F%2Fexodus.desync.com%3A6969"
    handle = lt.add_magnet_uri(ses, link, params)
    ses.start_dht()

    print 'downloading metadata...'
    while (not handle.has_metadata()):
        time.sleep(1)
    print 'got metadata, starting torrent download...'
    while (handle.status().state != lt.torrent_status.seeding):
        s = handle.status()
        state_str = ['queued', 'checking', 'downloading metadata', \
                'downloading', 'finished', 'seeding', 'allocating']
        print '%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % \
            (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, \
                s.num_peers, state_str[s.state])
        time.sleep(5)

if __name__ == '__main__':
    download()
