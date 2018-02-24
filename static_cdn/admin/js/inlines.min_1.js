(function(b){b.fn.formset=function(d){var a=b.extend({},b.fn.formset.defaults,d),e=b(this);d=e.parent();var k=function(a,f,l){var c=new RegExp("("+f+"-(\\d+|__prefix__))");f=f+"-"+l;b(a).prop("for")&&b(a).prop("for",b(a).prop("for").replace(c,f));a.id&&(a.id=a.id.replace(c,f));a.name&&(a.name=a.name.replace(c,f))},h=b("#id_"+a.prefix+"-TOTAL_FORMS").prop("autocomplete","off"),l=parseInt(h.val(),10),f=b("#id_"+a.prefix+"-MAX_NUM_FORMS").prop("autocomplete","off"),c=""===f.val()||0<f.val()-h.val();
e.each(function(f){b(this).not("."+a.emptyCssClass).addClass(a.formCssClass)});if(e.length&&c){var m;"TR"===e.prop("tagName")?(e=this.eq(-1).children().length,d.append('<tr class="'+a.addCssClass+'"><td colspan="'+e+'"><a href="javascript:void(0)">'+a.addText+"</a></tr>"),m=d.find("tr:last a")):(e.filter(":last").after('<div class="'+a.addCssClass+'"><a href="javascript:void(0)">'+a.addText+"</a></div>"),m=e.filter(":last").next().find("a"));m.click(function(c){c.preventDefault();c=b("#"+a.prefix+
"-empty");var g=c.clone(!0);g.removeClass(a.emptyCssClass).addClass(a.formCssClass).attr("id",a.prefix+"-"+l);g.is("tr")?g.children(":last").append('<div><a class="'+a.deleteCssClass+'" href="javascript:void(0)">'+a.deleteText+"</a></div>"):g.is("ul")||g.is("ol")?g.append('<li><a class="'+a.deleteCssClass+'" href="javascript:void(0)">'+a.deleteText+"</a></li>"):g.children(":first").append('<span><a class="'+a.deleteCssClass+'" href="javascript:void(0)">'+a.deleteText+"</a></span>");g.find("*").each(function(){k(this,
a.prefix,h.val())});g.insertBefore(b(c));b(h).val(parseInt(h.val(),10)+1);l+=1;""!==f.val()&&0>=f.val()-h.val()&&m.parent().hide();g.find("a."+a.deleteCssClass).click(function(c){c.preventDefault();g.remove();--l;a.removed&&a.removed(g);b(document).trigger("formset:removed",[g,a.prefix]);c=b("."+a.formCssClass);b("#id_"+a.prefix+"-TOTAL_FORMS").val(c.length);(""===f.val()||0<f.val()-c.length)&&m.parent().show();var d,e,h=function(){k(this,a.prefix,d)};d=0;for(e=c.length;d<e;d++)k(b(c).get(d),a.prefix,
d),b(c.get(d)).find("*").each(h)});a.added&&a.added(g);b(document).trigger("formset:added",[g,a.prefix])})}return this};b.fn.formset.defaults={prefix:"form",addText:"add another",deleteText:"remove",addCssClass:"add-row",deleteCssClass:"delete-row",emptyCssClass:"empty-row",formCssClass:"dynamic-form",added:null,removed:null};b.fn.tabularFormset=function(d){var a=b(this),e=function(l){b(a.selector).not(".add-row").removeClass("row1 row2").filter(":even").addClass("row1").end().filter(":odd").addClass("row2")},
k=function(){"undefined"!==typeof SelectFilter&&(b(".selectfilter").each(function(a,b){var c=b.name.split("-");SelectFilter.init(b.id,c[c.length-1],!1)}),b(".selectfilterstacked").each(function(a,b){var c=b.name.split("-");SelectFilter.init(b.id,c[c.length-1],!0)}))},h=function(a){a.find(".prepopulated_field").each(function(){var f=b(this).find("input, select, textarea"),c=f.data("dependency_list")||[],d=[];b.each(c,function(b,c){d.push("#"+a.find(".field-"+c).find("input, select, textarea").attr("id"))});
d.length&&f.prepopulate(d,f.attr("maxlength"))})};a.formset({prefix:d.prefix,addText:d.addText,formCssClass:"dynamic-"+d.prefix,deleteCssClass:"inline-deletelink",deleteText:d.deleteText,emptyCssClass:"empty-form",removed:e,added:function(a){h(a);"undefined"!==typeof DateTimeShortcuts&&(b(".datetimeshortcuts").remove(),DateTimeShortcuts.init());k();e(a)}});return a};b.fn.stackedFormset=function(d){var a=b(this),e=function(d){b(a.selector).find(".inline_label").each(function(a){a+=1;b(this).html(b(this).html().replace(/(#\d+)/g,
"#"+a))})},k=function(){"undefined"!==typeof SelectFilter&&(b(".selectfilter").each(function(a,b){var c=b.name.split("-");SelectFilter.init(b.id,c[c.length-1],!1)}),b(".selectfilterstacked").each(function(a,b){var c=b.name.split("-");SelectFilter.init(b.id,c[c.length-1],!0)}))},h=function(a){a.find(".prepopulated_field").each(function(){var d=b(this).find("input, select, textarea"),c=d.data("dependency_list")||[],e=[];b.each(c,function(b,c){e.push("#"+a.find(".form-row .field-"+c).find("input, select, textarea").attr("id"))});
e.length&&d.prepopulate(e,d.attr("maxlength"))})};a.formset({prefix:d.prefix,addText:d.addText,formCssClass:"dynamic-"+d.prefix,deleteCssClass:"inline-deletelink",deleteText:d.deleteText,emptyCssClass:"empty-form",removed:e,added:function(a){h(a);"undefined"!==typeof DateTimeShortcuts&&(b(".datetimeshortcuts").remove(),DateTimeShortcuts.init());k();e(a)}});return a}})(django.jQuery);