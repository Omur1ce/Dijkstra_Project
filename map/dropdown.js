 <body>

   <select id="list" style="padding: 10px;" onchange="getSelectValue();">
     <option value="js">JavaScript</option>
     <option value="php">PHP</option>
     <option value="c#">Csharp</option>
     <option value="java">Java</option>
     <option value="node">Node.js</option>
   </select>

    <script>
        function getSelectValue()
        {
            var selectedValue = document.getElementById("list").value;
            alert(selectedValue);
        }
        getSelectValue();
    </script>
 </body>