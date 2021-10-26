JAZZMIN_SETTINGS = {
    # title of the window
    "site_title": "自动评分判卷系统",

    # Title on the brand, and the login screen (19 chars max)
    "site_header": "HIT-SCORE",

    # square logo to use for your site, must be present in static files, used for favicon and brand on top left
    # "site_logo": "logo.png",

    # Welcome text on the login screen
    "welcome_sign": "欢迎使用哈尔滨工业大学自动评分判卷系统",

    # Copyright on the footer
    "copyright": "陈一帆熊皓项目组",

    # The model admin to search from the search bar, search bar omitted if excluded
    "search_model": "auth.User",

    # Field name on user model that contains avatar image
    "user_avatar": None,

    ############
    # Top Menu #
    ############

    # Links to put along the top menu
    "topmenu_links": [

        # Url that gets reversed (Permissions can be added)
        {"name": "主页", "url": "admin:index", "permissions": ["auth.view_user"]},

        # external url that opens in a new window (Permissions can be added)
        {"name": "反馈", "url": "mailto:1191000606@stu.hit.edu.cn/", "new_window": True},

        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},

        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"app": "user"},
    ],

    #############
    # User Menu #
    #############

    # Additional links to include in the user menu on the top right ("app" url type is not allowed)
    "usermenu_links": [
        {"name": "Support", "url": "mailto:1191000606@stu.hit.edu.cn/", "new_window": True},
        {"model": "auth.user"}
    ],

    #############
    # Side Menu #
    #############

    # Whether to display the side menu
    "show_sidebar": True,

    # Whether to aut expand the menu
    "navigation_expanded": False,

    # Hide these apps when generating side menu e.g (auth)
    "hide_apps": [],

    # Hide these models when generating side menu (e.g auth.user)
    "hide_models": [],

    # List of apps (and/or models) to base side menu ordering off of (does not need to contain all apps/models)
    "order_with_respect_to": [
        #apps
        'user',
        'equation',
    ],

    # Custom links to append to app groups, keyed on app name
    "custom_links": {
        # "books": [{
        #     "name": "Make Messages",
        #     "url": "make_messages",
        #     "icon": "fas fa-comments",
        #     "permissions": ["books.view_book"]
        # }]
    },

    # Custom icons for side menu apps/models See https://fontawesome.com/icons?d=gallery&m=free
    # for a list of icon classes
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",

        #apps
        'user.User': "fas fa-circle",
        "equation.Equation": "fas fa-circle",
    },
    # Icons that are used when one is not manually specified
    "default_icon_parents": "fas fa-circle",
    "default_icon_children": "fas fa-circle",

    #################
    # Related Modal #
    #################
    # Use modals instead of popups
    "related_modal_active": True,

    #############
    # UI Tweaks #
    #############
    # Relative paths to custom CSS/JS scripts (must be present in static files)
    "custom_css": None,
    "custom_js": None,
    # Whether to show the UI customizer on the sidebar
    "show_ui_builder": True,

    ###############
    # Change view #
    ###############
    # Render out the change view as a single form, or in tabs, current options are
    # - single
    # - horizontal_tabs (default)
    # - vertical_tabs
    # - collapsible
    # - carousel
    "changeform_format": "vertical_tabs",
    # override change forms on a per modeladmin basis
    "changeform_format_overrides": {"auth.user": "collapsible", "auth.group": "vertical_tabs", },
    # Add a language dropdown into the admin
    "language_chooser": False,
}
