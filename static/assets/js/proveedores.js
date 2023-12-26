(function() {
    "use strict";
    let intersectionCallback = (entries, observer) => {
        let entry = entries[0];
        if(entry.isIntersecting){
            let navbarItem = document.getElementById("proveedoresNavItem");
            navbarItem.classList.add("active");
        } else {
            let navbarItem = document.getElementById("proveedoresNavItem");
            navbarItem.classList.remove("active");
        }
    }
    var proveedores = document.getElementById("proveedores");
    let options = {
        rootMargin: "0px",
        threshold: [0.5, 0.8],
      };
      
    let observer = new IntersectionObserver(intersectionCallback, options);
    observer.observe(proveedores);
  })()