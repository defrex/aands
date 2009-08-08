//
// What Does This Do?
// In IE, unknow elements (everything new in html5) aren't able to be 
// styled in Internet Explorer. What this little hack does is call
// document.createElement on all of them so that they can be.
//
var e = "abbr,article,aside,audio,bb,canvas,datagrid,datalist,details,dialog,eventsource,figure,footer,header,hgroup,mark,menu,meter,nav,output,progress,section,time,video";
e = e.split(',');
for(var i=0;i<e.length;i++){
    document.createElement(e[i]);
}
