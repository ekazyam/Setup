# グローバル設定

|設定項目	|概要	|必須可否	|デフォルト値	|使い方	|
|:-----|:-----|:-----|:-----|:-----|
|dbdir|データベースファイルの保存ディレクトリ。|Yes|/var/lib/munin|dbdir /var/lib/munin|
|htmldir|HTMLの保存ディレクトリ。<br>グラフの更新周期に伴い、HTMLファイル(グラフ)が配置される。|Yes|/var/cache/munin/www|htmldir /var/cache/munin/www|
|logdir|ログが保存されるディレクトリ。|Yes|/var/log/munin|logdir /var/log/munin|
|rundir|調査中|Yes|/var/run/munin|rundir /var/run/munin|
|tmpldir|テンプレートファイルの設置ディレクトリ。<br>グラフ生成時にをmuninプロセスがtemplateファイルを置換し、HTMLファイルを出力する。|Yes|/etc/munin/templates|tmpldir /etc/munin/templates|
|fork|調査中||Yes||
|max_processes|測定データを各ノードから収集するプロセスの最大プロセス数。||16|max_processes 8|
|nsca|調査中||||
|domain_order|Muninに表示されるノードの順番を指定する。<br>未指定時はアルファベットを用いて昇順にソートされる。|||domain_order node1 node2 node3|
|max_graph_jobs|収集したデータからグラフを生成する際に走行する並列プロセス数。<br>munin-graphプロセス数に影響する。||6|max_graph_jobs 6|
|max_cgi_graph_jobs|収集したデータからグラフを生成する際に走行する並列プロセス数。<br>munin-cgi-graph またはmunin-fastcgi-graph jobs.のプロセス数に影響する。<br>max_graph_jobsと同数の指定を推奨。||6|max_cgi_graph_jobs 6|
|local_address|調査中|||||
