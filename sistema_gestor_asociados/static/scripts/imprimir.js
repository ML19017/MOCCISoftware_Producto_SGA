function imprimir(){
    window.print();
 }

function imprimir2(){
    var ficha = document.getElementById("central");
    var ventimp = window.open(' ', 'popimpr');
    ventimp.document.write(ficha.innerHTML);
    ventimp.document.close();
    ventimp.print();
    ventimp.close();
 }
