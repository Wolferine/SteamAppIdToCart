var listToAdd = [];
window.onload = function() {

    var sub = sessionStorage.getItem("sub");
    if (sub == null) {
        sub = 0;
    }
    if (sub >= listToAdd.length) {
        return;
    }

    addToCart(listToAdd[sub - listToAdd.length]);
    sessionStorage.setItem("sub", Number(sub) + 1);
    ;
}