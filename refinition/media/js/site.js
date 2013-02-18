;(function($){
var site = window.site = new function() 
{
    this.mode = 'preview';
    this.original_html = '';
    
    this.init = function() 
    {
        this.toggle_mode();
        this.editing_interactions();   
    };

    this.toggle_mode = function()
    {
        var self = this;
        
        $('#toggleEdit').click(function(e)
        {
            e.preventDefault();
            
            (self.mode == 'preview') ? self.activate_edit_mode() : '';
        });
        
        $('#interface .cancel').live('click', function(e)
        {
            e.preventDefault();
            
            $('#latestVersion').html(self.original_html);
            
            self.activate_preview_mode();            
        });
        
        $('#interface .save').live('click', function(e) 
        {            
            e.preventDefault();

            self.activate_preview_mode();
            
            var html = $('#latestVersion').html();

            Dajaxice.terms.save_version(self.save_version_callback, {'html': html });				    
        });        

       $('#interface #versions a').live('mouseover', function(e) 
       {
           e.preventDefault();

           var slug = $(this).attr('id');

           $('#loader').show();
           Dajaxice.terms.load_version(self.load_version_callback, {'version_slug': slug});				    
       });  
       
       $('#interface #versions a').live('mouseout', function(e) 
       {
           e.preventDefault();

           self.activate_edit_mode();
       });        

       $('#interface #versions a').live('click', function(e) 
       {
           e.preventDefault();

           var slug = $(this).attr('id');

           $('#loader').show();
           Dajaxice.terms.load_version(self.load_version_callback, {'version_slug': slug});				    
       });            
    };
    
    this.activate_edit_mode = function()
    {
        var self = this;
    
        self.original_html = $('#latestVersion').html();
            
        var html = '<a class="delete">x</a><a class="move">o</a>';
        var boxes = $('.box');
        
        for(var i=0; i<boxes.size(); i++)
        {
            var box = $(boxes).eq(i);
            
            // dragging & resizing a box
            $(box).draggable({ handle: '.move', cursor: 'move' }).resizable();            
            
            // add delete and move buttons
            $(box).append(html);
            
            // set class for styling
            $(box).addClass('edit');
        }
    
        $('#latestVersion').addClass('editing');
        
        $('#interface .controls, #interface ul#versions').fadeIn(300);
        
        self.mode = 'edit';
    };
    
    this.activate_preview_mode = function()
    {
        var self = this;
        
        $('.box').removeClass('edit');
        $('.delete, .move').remove();
        $('.ui-resizable-handle').remove();
    
        $('#latestVersion').removeClass('editing');
    
        $('#interface .controls, #interface ul#versions').fadeOut(300);
        
        self.mode = 'preview';        
    };
    
    this.editing_interactions = function()
    {
        var self = this;
        
        // deleting a box
        $('.box.edit .delete').live('click', function(e)
        {
           e.preventDefault();
           
           var box = $(this).parent();           
           
           if (confirm('Are you sure you want to delete this?'))
           {
               $(box).fadeOut(300, function() { $(box).remove(); });
           }
        });
        
        // edit box content
        $('.box.edit .content').live('click', function(e)
        {
            e.preventDefault();
            
            var box = $(this).parent();

            var original_html = $(this).html();
            
            var html = '<div class="controls"><a class="cancel">cancel</a><a class="save">save</a></div>';
            
            $(box).append(html);
            
            //$('*:tinymce').tinymce().remove();
                                    
            $('.content', box).tinymce(
            {   
                // Location of TinyMCE script
                script_url : STATIC_URL + 'js/tiny_mce/tiny_mce.js',

                // General options
                theme : "advanced",
                plugins : "style,advhr,advimage,advlink, iespell,inlinepopups",

                // Theme options
                theme_advanced_buttons1 : "bold,italic,underline,strikethrough,|fontsizeselect,|bullist,numlist,|,link,unlink,|,fontsizeselect,forecolor,backcolor",
                theme_advanced_toolbar_location : "top",
                theme_advanced_statusbar_location : "none",
                theme_advanced_resizing : true,

                // content CSS
                content_css : STATIC_URL + 'css/site.css',
            });
            
            console.log($('*:tinymce'));
            
            // canceling edits
            $('.cancel').live('click', function(e)
            {            
                var box = $(this).parent().parent();

                $('.content', box).tinymce().remove();

                $('.controls', box).remove();
                
                $('.content', box).html(original_html);
            });
            
            // saving edits
            $('.save').live('click', function(e)
            {            
                var box = $(this).parent().parent();

                $('.content', box).tinymce().remove();
                $('.controls', box).remove();
            });        
        });
        
        function randomString(length, chars) {
            var result = '';
            for (var i = length; i > 0; --i) result += chars[Math.round(Math.random() * (chars.length - 1))];
            return result;
        }
                
        // add box
        $('#latestVersion.editing').live('click', function(e)
        {
            // check that user is clicking on a blank area
            if ( e.target == this )
            {
                var id = randomString(10, '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ');

                var innerHtml = '<a class="delete">x</a><a class="move">o</a><div class="content" id="' + id + '">edit me!</div>';
                
                var box = $('<div>')
                            .addClass('box text edit')
                            .append(innerHtml)
                            .css({'left':e.pageX+'px', 'top':e.pageY+'px'})
                            .draggable({ handle: '.move', cursor: 'move' })
                            .resizable()
                            .appendTo("#latestVersion")
                            .fadeIn(300);
            }  
        });
    };


    this.load_version_callback = function(data)	
    {
        $('#loader').hide();

        $('#latestVersion').html(data);
    };


    this.save_version_callback = function(data)	
    {
        $('#latestVersion').html(data);
    };
};
})(jQuery);

$(document).ready(function()
{
	site.init();
});		