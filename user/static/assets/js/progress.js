 function btn1()
        {
            var a=document.getElementById("brand1");
            var b=document.getElementById("overall");
            var c=document.getElementById("brand2");
            var d=document.getElementById("brand3");
            if(a.style.display=="none")
            {
                b.style.display="none";
                c.style.display="none";
                d.style.display="none";
                a.style.display="block";
                
            }
            else
            {
                
                
            }
        }
        function btn2()
        {
            var c=document.getElementById("brand2");
            var b=document.getElementById("overall");
            var a=document.getElementById("brand1");
            var d=document.getElementById("brand3");
            if(a.style.display=="none")
            {
                
                b.style.display="none";
                a.style.display="none";
                d.style.display="none";
                c.style.display="block";
                
            }
            else{

                c.style.display="block";
                b.style.display="none";
                a.style.display="none";
                d.style.display="none";
                
            }
        }
        function btn3()
        {
            var c=document.getElementById("brand2");
            var b=document.getElementById("overall");
            var a=document.getElementById("brand1");
            var d=document.getElementById("brand3");
            if(a.style.display=="none")
            {
                d.style.display="block";
                b.style.display="none";
                c.style.display="none";
            }
            else{

                c.style.display="none";
                b.style.display="none";
                a.style.display="none";
                d.style.display="block";
                
            }
        }
