# グローバル設定

|設定項目	|概要	|チューニング	|必須可否	|デフォルト値	|使い方	|
|:-----|:-----|:-----|:-----|:-----|:-----|
|dbdir|データベースファイルの保存ディレクトリ。|-|Yes|/var/lib/munin|dbdir /var/lib/munin|
|htmldir|HTMLの保存ディレクトリ。<br>グラフの更新周期に伴い、HTMLファイル(グラフ)が配置される。|-|Yes|/var/cache/munin/www|htmldir /var/cache/munin/www|
|logdir|ログが保存されるディレクトリ。|-|Yes|/var/log/munin|logdir /var/log/munin|
|rundir|Muninの実行プロセスが可能されるディレクトリ。|-|Yes|/var/run/munin|rundir /var/run/munin|
|tmpldir|テンプレートファイルの設置ディレクトリ。<br>グラフ生成時にをmuninプロセスがtemplateファイルを置換し、HTMLファイルを出力する。|該当するファイル郡を置き換えることでMuninの外観を変更できる。<br>https://github.com/DaveMDS/munin_dynamic_template<br>https://github.com/jonnymccullagh/munstrap<br>https://github.com/Rauks/Moonstrap|Yes|/etc/munin/templates|tmpldir /etc/munin/templates|
|staticdir|テンプレートを置換するプログラムのの設置ディレクトリ。<br>グラフ生成時にをmuninプロセスがtemplateファイルを置換し、HTMLファイルを出力する。|該当するファイル郡を置き換えることでMuninの外観を変更できる。|Yes|/etc/munin/templates|tmpldir /etc/munin/static|
|fork|測定データを各ノードから収集する際にノードの数に応じてプロセスを並列で実行するか否かの指定。|Yes：収集時間が短くなる。ただし、Muninサーバの負荷が高くなる。<br>No：収集時間が長くなる。ただし、Muninサーバの負荷は低くなる。||Yes||
|max_processes|測定データを各ノードから収集するプロセスの最大プロセス数。|測定ノード数に応じて変更する。ただし、応じてMuninサーバの負荷が増減する。尚、並列に処理しない場合は0を指定する。<br>調整目安1：Muninデータ収集時間(全ノード分) > 収集周期<br>調整目安2：MuninサーバのCPU負荷が高い場合||16|max_processes 8|
|nsca||||||
|domain_order|MuninのWebUIに表示されるノードの順番を指定する。<br>標準ではアルファベット順の昇順で表示される。||||domain_order node1 node2 node3|
|max_graph_jobs|収集したデータからグラフを生成する際に走行する並列プロセス数。<br>munin-graphプロセス数に影響する。|測定対象のノードが多く、グラフ生成に時間を要する際に数値を増やす。ただし、応じてMuninサーバの負荷が変化する。||6|max_graph_jobs 6|
|max_cgi_graph_jobs|収集したデータからグラフを生成する際に走行する並列プロセス数。<br>munin-cgi-graph またはmunin-fastcgi-graph jobs.のプロセス数に影響する。|max_cgi_graph_jobsと同じ値にすること。||6|max_cgi_graph_jobs 6|
|local_address||||||
|contact.contact.command command||||||
|contact.contact.text text||||||
|contact.contact.max_messages number||||||
|contact.contact.always_send [warning] [critical]||||||
|contacts contact-list||||||
|[bar;example.com;foo.example.com]||||||
|[example.com;foo.example.com]||||||
|[foo.example.com]||||||
|cgitmpdir|Muninで利用するPHPを動作させる為のCGIのプロセスファイルが設置されるディレクトリ。|||/var/lib/munin/cgi-tmp|cgitmpdir /var/lib/munin/cgi-tmp|
|includedir|設定値を定義したファイル郡を読み込む。|設定の独立性が高くなり、設定値の再利用等が可能となる。||/etc/munin/munin-conf.d|includedir /etc/munin/munin-conf.d|
|graph_period|MuninのWebUI閲覧時に自動で画面がリフレッシュされる周期を指定する。|second：1秒毎に更新される。(負荷高)<br>minute：1分毎に更新される。(負荷中)<br>hour：1時間毎に更新される。(負荷低)||second|graph_period second|
|graph_strategy|グラフの生成方式を指定する。<br>デフォルトではcronモードが指定されており、/etc/cron.d/muninで指定された時間に応じてグラフ生成が成される。|cron：CRONモードで動作し、規定の周期でHTMLの生成を行う。WebUIを閲覧する利用者が多い場合に有効。Muninサーバに平均的に負荷がかかる。<br>cgi：CGIモードで動作し、WebUIにアクセスした時点でデータファイルから動的にHTMLの生成を行う。WebUIを閲覧する利用者が少ない場合に有効。Muninサーバにアクセスした時点に集中して負荷がかかる。||cron|graph_strategy cron|
|html_strategy|グラフの生成方式を指定する。graph_strategyパラメータと基本的に合わせる。|||cron|html_strategy cron|
|max_size_x|生成されるグラフのX軸ピクセル数。|グラフの解像度を変更可能。ただし、応じてグラフ生成時のメモリ使用率が増減する。<br>概算：1グラフ生成あたり、4000px * 4000px = 約1.92MB||4000|max_size_x 4000|
|max_size_y|生成されるグラフのY軸ピクセル数。|グラフの解像度を変更可能。ただし、応じてグラフ生成時のメモリ使用率が増減する。<br>概算：1グラフ生成あたり、4000px * 4000px = 約1.92MB||4000|max_size_y 4000|
|rrdcached_socket||||||





