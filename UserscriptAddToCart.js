//insert list here [y,x,z] int
var listToAdd = [];
var text = "";
listToAdd.forEach(id => {
    text = ("<a> <input type=\"hidden\" name=\"subid[]\" value=\""+ id + "\"> <\a>")
    document.getElementById("game_area_dlc_expanded").insertAdjacentHTML("afterend",text);
})
