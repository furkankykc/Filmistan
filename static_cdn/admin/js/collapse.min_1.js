(function(a){a(document).ready(function(){a("fieldset.collapse").each(function(b,c){0===a(c).find("div.errors").length&&a(c).addClass("collapsed").find("h2").first().append(' (<a id="fieldsetcollapser'+b+'" class="collapse-toggle" href="#">'+gettext("Show")+"</a>)")});a("fieldset.collapse a.collapse-toggle").click(function(b){a(this).closest("fieldset").hasClass("collapsed")?a(this).text(gettext("Hide")).closest("fieldset").removeClass("collapsed").trigger("show.fieldset",[a(this).attr("id")]):a(this).text(gettext("Show")).closest("fieldset").addClass("collapsed").trigger("hide.fieldset",
[a(this).attr("id")]);return!1})})})(django.jQuery);