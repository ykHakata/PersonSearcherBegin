DROP TABLE IF EXISTS last_name;
CREATE TABLE last_name (                            -- 名前(姓)
    id          INTEGER PRIMARY KEY AUTOINCREMENT,  -- 名前(姓) ID (例: 5)
    name        TEXT,                               -- 名前(姓) (例: '相川')
    ruby        TEXT,                               -- よみがな (例: 'あいかわ')
    create_on   TEXT,                               -- 登録日 (例: '2016-03-06 12:24:12')
    modify_on   TEXT                                -- 修正日 (例: '2016-03-06 12:24:12')
);

DROP TABLE IF EXISTS first_name;
CREATE TABLE first_name (                           -- 名前(名)
    id          INTEGER PRIMARY KEY AUTOINCREMENT,  -- 名前(名) ID (例: 5)
    name        TEXT,                               -- 名前(名) (例: '加納子')
    ruby        TEXT,                               -- よみがな (例: 'かなこ')
    create_on   TEXT,                               -- 登録日 (例: '2016-03-06 12:24:12')
    modify_on   TEXT                                -- 修正日 (例: '2016-03-06 12:24:12')
);
