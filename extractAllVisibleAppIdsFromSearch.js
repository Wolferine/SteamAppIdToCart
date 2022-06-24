var out = []
document.querySelectorAll(".search_result_row").forEach(ele => { if(ele.getHeight() > 30) out.push(ele.getAttribute("href"))})