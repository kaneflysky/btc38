<?php
	// 数据库连接基本信息
	$db_host = "localhost";
	$db_user = "btc38";
	$db_pass = "29EZjNEsNBcWnfVJ";
	$db_name = "btc38";
	
	// sql 语句
	$query = "select updateTime, holders from btc38info where coin = 'btc' order by updateTime";
	
	// 数据库连接
	$link = mysql_connect($db_host,$db_user,$db_pass);
	
	// select DB
	mysql_select_db($db_name,$link);	
	
	// 执行sql语句
	$rows = mysql_query($query,$link);
	
	// 将数据存入
	$datas = array();
	while($row = mysql_fetch_row($rows) ) {
		$datas[] = $row;
	}
	
	// 输出 json字符串
	// 实例
	// [["100","1","2013-12"],["475","11","2014-01"],["480","7","2014-02"],["342","10","2014-03"],["27","4","2014-04"]]
	echo json_encode($datas);
?>