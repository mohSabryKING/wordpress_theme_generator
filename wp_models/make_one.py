import os 

print(("-"*20)+"\n")
max_wp_models=int(input("\nadd your max num of models:"))

html_cont_model="""
      <!DOCTYPE html>
<html lang="en">
<head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width',' initial-scale=1.0">
      <title>Document</title>
</head>
<header></header>
<body>
      
</body>
<footer></footer>
</html>
      """

php_cont_model="""
      <!DOCTYPE html>
<html lang="en">
<head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width',' initial-scale=1.0">
      <title>Document</title>
</head>
<header>
<?php get_header() ?>
</header>
<body>
      <?php get_sidebar() ?>
</body>
<footer>

<?php get_footer() ?>
</footer>
</html>
      """

css_class_list=['ab-top-menu','display-name','ab-sub-wrapper','searchform','screen-reader-shortcut','screen-reader-text','screen-reader-text','ab-icon','page_item page-item-2','page_item.page-item-18','page_item.page-item-22','page-template-default','page_item.page-item-20','page_item.page-item-3','ab-submenu','ab-top-menu','description','nojq.nojs']



for f in range(max_wp_models):
      act1=os.mkdir("model_"+str(f+1))
      act2=os.system("nul>model_"+str(f+1)+"/style.css")
      act2_1=open("model_"+str(f+1)+"/style.css","w+")
      for c in range(len(css_class_list)):
            act2_1.write("."+css_class_list[c]+"{"+"}\n")
      act2_1.close()
      act3=os.system("nul>model_"+str(f+1)+"/index.php")
      act3_1=open("model_"+str(f+1)+"/index.php","w+")
      act3_1.write(php_cont_model)
      act3_1.close()

      act4=os.system("nul>model_"+str(f+1)+"/index.html")
      act4_1=open("model_"+str(f+1)+"/index.html","w+")
      act4_1.write(html_cont_model)
      act4_1.close()

      act5=os.system("nul>model_"+str(f+1)+"/model.js")
      5
      

      






print(("-"*20)+"\n")