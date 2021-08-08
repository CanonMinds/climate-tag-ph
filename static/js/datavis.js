/*******************************************
    Global functions for table display
    for summary
*******************************************/

/*
function addSummaryElement creates cards that
represent rows of the summary table:
    string label - left column text
    string value - right column text
*/
function addSummaryElement(label, value) {
    let card = document.createElement("div");
    card.className = "summary-card";
    card.id = label.replace(/\s+/g, '');

    let left = document.createElement("div");
    left.className = "summary-value";
    let node_value = document.createTextNode(value);
    left.appendChild(node_value);

    let right = document.createElement("div");
    right.className = "summary-label";
    let node_label = document.createTextNode(label);
    right.appendChild(node_label);

    card.appendChild(left);
    card.appendChild(right);
    return card;
}

/*
function addCards forms the table div displaying
numerical data of summary:
dom table - dom element housing summary
    string type - used for getting colors depending
        on model type (ex. hoa, pap)
    boolean limitCards - limit summary rows if true.
        collates remaining data into "Others"
    string value - identifies which data summary
        to display, contains eligible key in list
    dict list - key:[value] pairs where key is the
        summary identifiers and value is a dict of
        form ['grouper':value,'count':value]
*/
function addCards(table, type, limitCards, value, list) {
    table.textContent = '';
    let max_cards = 5, 
        ctr = 0,
        total = 0,
        shown = 0,
        limit=limitCards;

    for (element in list) {
        if (value ? element == value : true) {
            for (sub in list[element]) {
                if (limit ? ctr < max_cards : true) {
                    var child = addSummaryElement(
                        list[element][sub]['grouper'],
                        list[element][sub]['count']
                        );
                    if (!limit) {
                        child.children[1].style.color = getColor(type,'css',list[element][sub]['grouper']);
                    }
                    table.appendChild(child);
                    shown += list[element][sub]['count'];
                }
                total += list[element][sub]['count'];
                ctr+=1;
            }
        }
    }
    table.insertBefore(addSummaryElement('Total',total),table.childNodes[0]);
    if (limit && shown != total) {
        table.appendChild(addSummaryElement('Others',total-shown));
    }
}

/*******************************************
    Color function
*******************************************/

/*
function getColor identifies correct colors for markers/text
according to identifier
    string type - used for getting colors depending
        on model type (ex. hoa, pap)
    string format - identifies what format of color
        is returned, if 'css' returns variable name.
        otherwise, it returns marker variable for map
    string identifier - value that seeks color representation
*/
function getColor(type, format, identifier) {
    identifier = identifier.toLowerCase();
    switch(type) {
        case "hoa":
            switch(identifier) {
                case 'community mortgage program':
                    if (format == 'css') {return 'var(--marker-red)';}else {return redIcon;}
                case 'federation':
                    // not assigned by HLURB
                    if (format == 'css') {return 'var(--marker-yellow)';}else {return yellowIcon;}
                case 'group land acquisition and development program':
                    // not assigned by HLURB
                    if (format == 'css') {return 'var(--marker-gold)';}else {return goldIcon;}
                case 'land tenure assistance program':
                    if (format == 'css') {return 'var(--marker-orange)';}else {return orangeIcon;}
                case 'nha projects':
                    // not assigned by HLURB
                    if (format == 'css') {return 'var(--marker-violet)';}else {return violetIcon;}
                case 'neighborhood':
                    if (format == 'css') {return 'var(--marker-green)';}else {return greenIcon;}
                case 'regular':
                    if (format == 'css') {return 'var(--marker-blue)';}else {return blueIcon;}
                default:
                    if (format == 'css') {return 'var(--marker-gray)';}else {return grayIcon;}
            }
            break;

        case "pap":
            switch(identifier) {
                case 'completed':
                    if (format == 'css') {return 'var(--marker-green)';}else {return greenIcon;}
                case 'pipelined':
                    if (format == 'css') {return 'var(--marker-gold)';}else {return goldIcon;}
                case 'ongoing':
                    if (format == 'css') {return 'var(--marker-blue)';}else {return blueIcon;}
                default:
                    if (format == 'css') {return 'var(--marker-gray)';}else {return grayIcon;}
            }
            break;

        case "devproj":
            switch(identifier) {
                case 'residential':
                    if (format == 'css') {return 'var(--marker-red)';}else {return redIcon;}
                case 'non-residential':
                    if (format == 'css') {return 'var(--marker-gold)';}else {return goldIcon;}
                case 'compliance':
                    if (format == 'css') {return 'var(--marker-blue)';}else {return blueIcon;}
                default:
                    if (format == 'css') {return 'var(--marker-green)';}else {return greenIcon;}
            }
            break;

        case "ppfp":
            switch(identifier) {
                case 'updated':
                    if (format == 'css') {return 'var(--marker-green)';} else {return greenIcon;}
                case 'for updating':
                    if (format == 'css') {return 'var(--marker-gold)';} else {return goldIcon;}
                default:
                    if (format == 'css') {return 'var(--marker-red)';} else {return redIcon;}
            }
            break;

        case "lsp":
            switch(identifier) {
                case 'updated':
                    if (format == 'css') {return 'var(--marker-green)';} else {return greenIcon;}
                case 'for updating':
                    if (format == 'css') {return 'var(--marker-gold)';} else {return goldIcon;}
                case 'for approval':
                    if (format == 'css') {return 'var(--marker-blue)';} else {return blueIcon;}
                default:
                    if (format == 'css') {return 'var(--marker-red)';} else {return redIcon;}
            }
            break;

        case "clup":
            switch(identifier) {
                case 'updated':
                    if (format == 'css') {return 'var(--marker-green)';}
                case 'for updating':
                    if (format == 'css') {return 'var(--marker-gold)';}
                case 'no clup':
                    if (format == 'css') {return 'var(--marker-red)';}
                default:
                    if (format == 'css') {return 'var(--marker-gray)';}
            }
            break;

        case 'dhsud':
            switch(identifier) {
                case 'residential':
                    if (format == 'css') {return 'var(--marker-green)';}
                case 'nonresidential':
                    if (format == 'css') {return 'var(--marker-orange)';}
                case 'compliance':
                    if (format == 'css') {return 'var(--marker-blue)';}
            }
            break;

        case 'ilhud':
            switch(identifier) {
                case 'government idle land':
                    if (format == 'css') {return 'var(--marker-red)';}else {return redIcon;}
                case 'marginal agricultural land':
                    if (format == 'css') {return 'var(--marker-yellow)';}else {return yellowIcon;}
                case 'proclaimed government lands for housing purposes':
                    if (format == 'css') {return 'var(--marker-gold)';}else {return goldIcon;}
                case 'unregistered or abandoned land':
                    if (format == 'css') {return 'var(--marker-orange)';}else {return orangeIcon;}
                case 'undeveloped and vacant land zoned for residential purposes':
                    if (format == 'css') {return 'var(--marker-green)';}else {return greenIcon;}
                default:
                    if (format == 'css') {return 'var(--marker-gray)';}else {return grayIcon;}
            }
            break;

        default:
            return 'var(--marker-black)';
    }

    return 'var(--marker-black)';
}

/*******************************************
    Global settings for Chartjs
    https://www.chartjs.org/docs/latest/
*******************************************/

var chartColors = [
                    "#2A81CB",
                    "#FFD326",
                    "#f34e4a",
                    "#3fbd3f",
                    "#f5ad0d",
                    "#CAC428",
                    "#9C2BCB",
                    "#2f92ca",
                    "#3fbd3f",
                    "#ff2a2a"
                ];

/*
function getDefaultChartColors returns list of
label colors taken from the variable chartColors
    integer amount - number of labels
*/
function getDefaultChartColors(amount) {
    let colors = [];
    let ctr;

    for (ctr = 0; ctr < amount; ctr++) {
        colors.push(chartColors[ctr%chartColors.length]);
    }

    return colors;
}

// Chart defaults
Chart.defaults.global.defaultFontFamily = "'OpenSans', sans-serif";
Chart.defaults.global.legend.display = false;

/*
function getHex returns the hex value represented
by the css variables declared in site_base.css
    string color - variable name as declared
    dom document
*/
function getHex(color, document) {
    let style = getComputedStyle(document.documentElement);

    return style.getPropertyValue(color.replace('var(','').replace(')','')).replace(' ','');
}

/*
function getLabelsDataColors extracts 3 lists from the
dictionary to be used in the chart
    string type - used for getting colors depending
        on model type (ex. hoa, pap)
    string query - if exists, it is used as key to
        find specific summary value
    dict list - key:[value] pairs where key is the
        summary identifiers and value is a dict of
        form ['grouper':value,'count':value]
    dom document - for getHex function
*/
function getLabelsDataColors(type, query, list, document) {
    var labels = [],
        data = [],
        colors = [];

    for (element in list) {
        if (query ? element == query : true) {
            for (property in list[element]) {
                labels.push(list[element][property]['grouper']);
                data.push(list[element][property]['count']);
                colors.push(getHex(getColor(type,'css',list[element][property]['grouper']),document));
            }
        }
    }

    return [labels,data,colors];
}

