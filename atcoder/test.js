var Distance = [
    [0,2,8,4,-1,-1,-1],
    [2,0,-1,-1,3,-1,-1],
    [8,-1,0,-1,2,3,-1],
    [4,-1,-1,0,-1,8,-1],
    [-1,3,2,-1,0,-1,9],
    [-1,-1,3,8,-1,0,3],
    [-1,-1,-1,-1,9,3,0]
  ];
  var sp = 0;
  var dp = 6;
  var nPoint = 7;
  var sRoute = [];
  var sDist = 0;
  
  ShortestPath(Distance, nPoint, sp, dp, sRoute, 0);
  
  function ShortestPath(Distance, nPoint, sp, dp, sRoute, sDist)
  {
    var pDist = new Array(nPoint);
    var pRoute = new Array(nPoint);
    var pFixed = new Array(nPoint);
    var sPoint, i, j, newDist;
    
    sDist = Infinity; //Infinityは正の無限大を表す定数
    for (i=0; i<nPoint; i++) {
      sRoute[i] = -1; //経由地点数が6以下だと最後の出力に-1が出てしまうため初期化不要かも
      pDist[i] = Infinity;
        pFixed[i] = false;
        pRoute[i] = 0; //設問ではpRouteの初期化処理がなかったため追加しました。
    }
    pDist[sp] = 0;
    while (true) {
      i = 0;
      while (i < nPoint) {
        if (!pFixed[i]) {
          break;
        }
        i = i + 1;
      }
      if (i == nPoint) {
        break;
      }
      for (j=i+1; j<nPoint; j++) {
        if (!pFixed[j] && pDist[j] < pDist[i]) {
          i = j;
        }
      }
      sPoint = i;
      pFixed[sPoint] = true;
      document.write('sPoint='+sPoint+'<br>');
      for (j=0; j<nPoint; j++) {
        if (Distance[sPoint][j] > 0 && !pFixed[j]) {
          newDist = pDist[sPoint] + Distance[sPoint][j];
          if (newDist < pDist[j]) {
            pDist[j] = newDist;
            pRoute[j] = sPoint;
          }
        }
      }
      document.write('pFixed='+pFixed+'<br>');
      document.write('pDist='+pDist+'<br>');
      document.write('pRoute='+pRoute+'<br><br>');
    }
    sDist = pDist[dp];
    j = 0;
    i = dp;
    while (i != sp) {
      sRoute[j] = i;
      i = pRoute[i];
      j = j + 1;
    }
    sRoute[j] = sp;
    //最短距離と目的地→出発地に向かう経由地を出力
    document.write('最短距離 sDist='+sDist+'<br>');
    document.write('経由地点 sRoute='+sRoute+'<br>');
  }