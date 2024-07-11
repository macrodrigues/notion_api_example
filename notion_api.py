import os
import requests
import dotenv
dotenv.load_dotenv('keys.env')

token = os.getenv('token')

headers = {
    'Authorization': f"Bearer {token}",
    'Content-Type': 'application/json',
    'Notion-Version': '2022-06-28'}

# retrive pages
search_response = requests.post(
    'https://api.notion.com/v1/search',
    headers=headers,
    timeout=5000)

# write
search_results = search_response.json()["results"]
for i, element in enumerate(search_results):
    if search_results[i]["id"] == "dec31e5f-fda6-4830-86da-dd4860601cbb":
        parent_page_id = search_results[i]["id"]
        break

create_page_body = {
    "cover": {
        "type": "external",
        "external": {
            "url": (
                "https://images.unsplash.com/photo-1684103296711-de5797853"
                "fe5?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid="
                "M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D")
        }},
    "icon": {
        "type": "emoji",
        "emoji": "📈"
        },
    "parent": {
        "page_id": parent_page_id},  # this is the parent page id
    "properties": {
        "title": {
            "title": [{"text": {"content": "Week 28 Ultimate Report"}}]}
    },
    "children": [{
        "object": "block",
        "type": "paragraph",
        "paragraph": {
            "rich_text": [{
                "text": {"content": (
                    "This is an example of a report, you can use this "
                    "template and make your own changes\n")}}]}
        }, {
        "object": "block",
        "type": "numbered_list_item",
        "numbered_list_item": {
            "rich_text": [{
                "text": {
                    "content": (
                        "What are the top domains people search on "
                        "social networks?")},
                "annotations": {
                    "bold": True}},
                ]},
        }, {
        "object": "block",
        "type": "numbered_list_item",
        "numbered_list_item": {
            "rich_text": [{
                "text": {
                    "content": (
                        "What are the most recent news?")},
                "annotations": {
                    "bold": True}},
                ]},
        }, {
        "object": "block",
        "type": "divider",
        "divider": {}
        }, {
        "object": "block",
        "heading_1": {
            "rich_text": [{
                "text": {"content": ("1. What are the top domains people "
                                     "search on social networks?")}}]}
        }, {
        "object": "block",
        "type": "paragraph",
        "paragraph": {
            "rich_text": [{
                "text": {"content": "Look at this beautiful chart!"}}]}
        }, {
        "object": "block",
        "type": "embed",
        "embed": {
            "url": (
                "https://macrodrigues.github.io/notion_api_example/"
                "bar_domains.html")}
        },]
    }

create_response = requests.post(
    "https://api.notion.com/v1/pages",
    json=create_page_body,
    headers=headers,
    timeout=5000)

print(create_response.json())

    #         "object": BLOCK,
    #         "type": "divider",
    #         "divider": {}
    #         }, {
    #         "object": BLOCK,
    #         "heading_1": {
    #             "rich_text": [{
    #                 "text": {"content": CHAPTER_1}}]}
    #         }, {
    #         "object": BLOCK,
    #         "type": "paragraph",
    #         "paragraph": {
    #             "rich_text": [{
    #                 "text": {"content": CHAPTER_1_INTRO}}]}
    #         }, {
    #         "object": BLOCK,
    #         "type": "embed",
    #         "embed": {
    #             "url": (
    #                 "https://hub.modal.systems/notion/"
    #                 f"bar_dialogs_{WEEK_NUM}_{END_YEAR}.html")}
    #         }, {
    #         "object": BLOCK,
    #         "heading_1": {
    #             "rich_text": [{
    #                 "text": {"content": CHAPTER_2}}]}
    #         }, {
    #         "object": BLOCK,
    #         "type": "paragraph",
    #         "paragraph": {
    #             "rich_text": [{
    #                 "text": {"content": CHAPTER_2_INTRO}}]}
    #         }, {
    #         "object": BLOCK,
    #         "type": "embed",
    #         "embed": {
    #             "url": (
    #                 "https://hub.modal.systems/notion/"
    #                 f"pie_domains_{WEEK_NUM}_{END_YEAR}.html")}
    #         }, {
    #         "object": BLOCK,
    #         "heading_1": {
    #             "rich_text": [{
    #                 "text": {"content": CHAPTER_3}}]}
    #         }, {
    #         "object": BLOCK,
    #         "type": "paragraph",
    #         "paragraph": {
    #             "rich_text": [{
    #                 "text": {"content": CHAPTER_3_INTRO}}]}
    #         }, {
    #         "object": BLOCK,
    #         "type": "embed",
    #         "embed": {
    #             "url": (
    #                 "https://hub.modal.systems/notion/"
    #                 f"bar_room_services_{WEEK_NUM}_{END_YEAR}.html")}
    #         }, {
    #         "object": BLOCK,
    #         "heading_1": {
    #             "rich_text": [{
    #                 "text": {"content": CHAPTER_4}}]}
    #         }, {
    #         "object": BLOCK,
    #         "type": "paragraph",
    #         "paragraph": {
    #             "rich_text": [{
    #                 "text": {"content": CHAPTER_4_INTRO}}]}
    #         }, {
    #         "object": BLOCK,
    #         "type": "table",
    #         "table": {
    #             "table_width": 2,
    #             "has_column_header": True,
    #             "has_row_header": True,
    #             "children": [{
    #                 "object": BLOCK,
    #                 "type": "table_row",
    #                 "table_row": {
    #                     "cells": [
    #                         [{
    #                             "type": "text",
    #                             "text": {"content": "Hotels"}}],
    #                         [{
    #                             "type": "text",
    #                             "text": {"content": "Sessions"}}],
    #                     ]
    #                 }
    #             }, {
    #                 "object": BLOCK,
    #                 "type": "table_row",
    #                 "table_row": {
    #                     "cells": [
    #                         [{
    #                             "type": "text",
    #                             "text": {
    #                                 "content": ("NH Collection Barcelona "
    #                                             "Gran Hotel Calderón")}}],
    #                         [{
    #                             "type": "text",
    #                             "text": {
    #                                 "content": f"{N_SESSIONS_CALDERON}"}}],
    #                     ]
    #                 }
    #             }, {
    #                 "object": BLOCK,
    #                 "type": "table_row",
    #                 "table_row": {
    #                     "cells": [
    #                         [{"text": {
    #                             "content":
    #                                 "NH Collection Madrid Gran Via"}}],
    #                         [{"text": {"content": f"{N_SESSIONS_GRAN_VIA}"}}],
    #                     ]
    #                 }
    #             }, {
    #                 "object": BLOCK,
    #                 "type": "table_row",
    #                 "table_row": {
    #                     "cells": [
    #                         [{"text": {
    #                             "content":
    #                                 "NH Collection Madrid Paseo del Prado"}}],
    #                         [{"text": {"content": f"{N_SESSIONS_PRADO}"}}],
    #                     ]
    #                 }
    #             }, {
    #                 "object": BLOCK,
    #                 "type": "table_row",
    #                 "table_row": {
    #                     "cells": [
    #                         [{"text": {
    #                             "content":
    #                                 "NH Collection Madrid Abascal"}}],
    #                         [{"text": {"content": f"{N_SESSIONS_ABASCAL}"}}],
    #                     ]
    #                 }
    #             }]
    #         },

    #     }, {
    #         "object": BLOCK,
    #         "type": "paragraph",
    #         "paragraph": {
    #             "rich_text": [{
    #                 "text": {"content": CHAPTER_4_INTRO_2}}]}
    #         }, {
    #         "object": BLOCK,
    #         "heading_3": {
    #             "rich_text": [{
    #                 "text": {
    #                     "content": (
    #                         "Número de sesiones en NH Collection "
    #                         "Barcelona Gran Hotel Calderón")}}],
    #             "is_toggleable": True,
    #             "children": [
    #                 {
    #                     "object": BLOCK,
    #                     "type": "embed",
    #                     "embed": {
    #                         "url": (
    #                             "https://hub.modal.systems/notion/bar_sessions"
    #                             f"_NHC0001_{WEEK_NUM}_{END_YEAR}.html")}}]
    #         }}, {
    #         "object": BLOCK,
    #         "heading_3": {
    #             "rich_text": [{
    #                 "text": {
    #                     "content": (
    #                         "Número de sesiones en "
    #                         "NH Collection Madrid Gran Via")}}],
    #             "is_toggleable": True,
    #             "children": [
    #                 {
    #                     "object": BLOCK,
    #                     "type": "embed",
    #                     "embed": {
    #                         "url": (
    #                             "https://hub.modal.systems/notion/bar_sessions"
    #                             f"_NHGV0001_{WEEK_NUM}_{END_YEAR}.html")}}]
    #         }}, {
    #         "object": BLOCK,
    #         "heading_3": {
    #             "rich_text": [{
    #                 "text": {
    #                     "content": (
    #                         "Número de sesiones en "
    #                         "NH Collection Madrid Paseo del Prado")}}],
    #             "is_toggleable": True,
    #             "children": [
    #                 {
    #                     "object": BLOCK,
    #                     "type": "embed",
    #                     "embed": {
    #                         "url": (
    #                             "https://hub.modal.systems/notion/bar_sessions"
    #                             f"_NHP0001_{WEEK_NUM}_{END_YEAR}.html")}}]
    #         }}, {
    #         "object": BLOCK,
    #         "heading_3": {
    #             "rich_text": [{
    #                 "text": {
    #                     "content": (
    #                         "Número de sesiones en "
    #                         "NH Collection Madrid Abascal")}}],
    #             "is_toggleable": True,
    #             "children": [
    #                 {
    #                     "object": BLOCK,
    #                     "type": "embed",
    #                     "embed": {
    #                         "url": (
    #                             "https://hub.modal.systems/notion/bar_sessions"
    #                             f"_NHA0001_{WEEK_NUM}_{END_YEAR}.html")}}]
    #         }}, {
    #         "object": BLOCK,
    #         "heading_1": {
    #             "rich_text": [{
    #                 "text": {"content": CHAPTER_5}}]}
    #         }, {
    #         "object": BLOCK,
    #         "type": "paragraph",
    #         "paragraph": {
    #             "rich_text": [{
    #                 "text": {"content": CHAPTER_5_INTRO}}]}
    #         }, {
    #         "object": BLOCK,
    #         "type": "embed",
    #         "embed": {
    #             "url": (
    #                 "https://hub.modal.systems/notion/"
    #                 f"bar_sessions_times_{WEEK_NUM}_{END_YEAR}.html")}
    #         }, {
    #         "object": BLOCK,
    #         "heading_1": {
    #             "rich_text": [{
    #                 "text": {"content": CHAPTER_6}}]}
    #         }, {
    #         "object": BLOCK,
    #         "type": "paragraph",
    #         "paragraph": {
    #             "rich_text": [{
    #                 "text": {"content": CHAPTER_6_INTRO}}]}
    #         }, {
    #         "object": BLOCK,
    #         "type": "embed",
    #         "embed": {
    #             "url": (
    #                 "https://hub.modal.systems/notion/pie_use_cases"
    #                 f"_{WEEK_NUM}_{END_YEAR}.html")}
    #         }, {
    #         "object": BLOCK,
    #         "type": "paragraph",
    #         "paragraph": {
    #             "rich_text": [
    #                 {"text": {
    #                     "content":
    #                         "La utilización de la app NH ha ahorrado "}},
    #                 {
    #                     "text": {"content": f"{df_usecases['count'].sum()}"},
    #                     "annotations": {
    #                         "bold": True,
    #                         "color": "orange"}},
    #                 {"text": {
    #                     "content":
    #                         (
    #                             f" minutos entre "
    #                             f"{START_MONTH} {START_YEAR} y "
    #                             f"{END_MONTH} {END_YEAR}, "
    #                             "lo que equivale a ")}},
    #                 {
    #                     "text": {
    #                         "content": (
    #                             f"{round(df_usecases['count'].sum()/60, 1)}")},
    #                     "annotations": {
    #                         "bold": True,
    #                         "color": "orange"}},
    #                 {"text": {
    #                     "content": " horas."}},]}
    #         }, {
    #         "object": BLOCK,
    #         "heading_1": {
    #             "rich_text": [{
    #                 "text": {"content": CHAPTER_7}}]}
    #         }, {
    #         "object": BLOCK,
    #         "type": "paragraph",
    #         "paragraph": {
    #             "rich_text": [{
    #                 "text": {"content": CHAPTER_7_INTRO}}]}
    #         }, {
    #         "object": BLOCK,
    #         "heading_3": {
    #             "rich_text": [{
    #                 "text": {
    #                     "content": (
    #                         "Pedidos y valor generado en "
    #                         "NH Collection Barcelona Gran Hotel Calderón")}}],
    #             "is_toggleable": True,
    #             "children": [
    #                 {
    #                     "object": BLOCK,
    #                     "type": "embed",
    #                     "embed": {
    #                         "url": (
    #                             "https://hub.modal.systems/notion/bar_orders"
    #                             f"_NHC0001_{WEEK_NUM}_{END_YEAR}.html")}}]
    #         }}, {
    #         "object": BLOCK,
    #         "heading_3": {
    #             "rich_text": [{
    #                 "text": {
    #                     "content": (
    #                         "Pedidos y valor generado en "
    #                         "NH Collection Madrid Gran Via")}}],
    #             "is_toggleable": True,
    #             "children": [
    #                 {
    #                     "object": BLOCK,
    #                     "type": "embed",
    #                     "embed": {
    #                         "url": (
    #                             "https://hub.modal.systems/notion/bar_orders"
    #                             f"_NHGV0001_{WEEK_NUM}_{END_YEAR}.html")}}]
    #         }}, {
    #         "object": BLOCK,
    #         "heading_3": {
    #             "rich_text": [{
    #                 "text": {
    #                     "content": (
    #                         "Pedidos y valor generado en "
    #                         "NH Collection Madrid Paseo del Prado")}}],
    #             "is_toggleable": True,
    #             "children": [
    #                 {
    #                     "object": BLOCK,
    #                     "type": "embed",
    #                     "embed": {
    #                         "url": (
    #                             "https://hub.modal.systems/notion/bar_orders"
    #                             f"_NHP0001_{WEEK_NUM}_{END_YEAR}.html")}}]
    #         }}, {
    #         "object": BLOCK,
    #         "type": "heading_3",
    #         "heading_3": {
    #             "rich_text": [{
    #                 "type": "text",
    #                 "text": {
    #                     "content": ("Pedidos y valor generado en "
    #                                 "NH Collection Madrid Abascal")}}],
    #             "is_toggleable": True,
    #             "children": [
    #                 {
    #                     "object": BLOCK,
    #                     "type": "embed",
    #                     "embed": {
    #                         "url": (
    #                             "https://hub.modal.systems/notion/bar_orders_"
    #                             f"NHA0001_{WEEK_NUM}_{END_YEAR}.html")}}]
    #         }}, {
    #         "object": BLOCK,
    #         "type": "paragraph",
    #         "paragraph": {
    #             "rich_text": [{
    #                 "text": {
    #                     "content": (
    #                         "El valor promedio de transacción en el total "
    #                         "de todos los pedidos realizados en todos los "
    #                         "restaurantes es de ")}}, {
    #                 "text": {"content": f"{ORDER_MEAN} €"},
    #                 "annotations": {
    #                         "bold": True,
    #                         "color": "orange"}
    #                 }, {
    #                 "text": {"content": "."}
    #                 }]}
    #         }, {
    #         "object": BLOCK,
    #         "heading_1": {
    #             "rich_text": [{
    #                 "text": {"content": CHAPTER_8}}]}
    #         }, {
    #         "object": BLOCK,
    #         "type": "paragraph",
    #         "paragraph": {
    #             "rich_text": [{
    #                 "text": {"content": CHAPTER_8_INTRO}}]}
    #         }, {
    #         "object": BLOCK,
    #         "type": "embed",
    #         "embed": {
    #             "url": (
    #                 "https://hub.modal.systems/notion/bar_qr_codes"
    #                 f"_{WEEK_NUM}_{END_YEAR}.html")}
    #         }, {
    #         "object": BLOCK,
    #         "heading_1": {
    #             "rich_text": [{
    #                 "text": {"content": CHAPTER_9}}]}
    #         }, {
    #         "object": BLOCK,
    #         "type": "paragraph",
    #         "paragraph": {
    #             "rich_text": [{
    #                 "text": {"content": CHAPTER_9_INTRO}}]}
    #         }, {
    #         "object": BLOCK,
    #         "type": "heading_3",
    #         "heading_3": {
    #             "rich_text": [{
    #                 "type": "text",
    #                 "text": {
    #                     "content": (
    #                         "Haz clic para abrir las imágenes "
    #                         "y sus estadísticas")}}],
    #             "is_toggleable": True,
    #             "children": [
    #                 {
    #                     "object": BLOCK,
    #                     "type": "image",
    #                     "image": {
    #                         "type": "external",
    #                         "external": {
    #                             "url": (
    #                                 f"{df_banners['banner'].unique()[0]}")}
    #                         }},
    #                 {
    #                     "object": BLOCK,
    #                     "type": "bulleted_list_item",
    #                     "bulleted_list_item": {
    #                         "rich_text": [{
    #                             "type": "text",
    #                             "text": {"content": "Request Type: "},
    #                             "annotations": {"bold": True}
    #                         }, {
    #                             "type": "text",
    #                             "text": {"content": "Survey"},
    #                             "annotations": {"color": "orange"}
    #                         }]}
    #                 }, {
    #                     "object": BLOCK,
    #                     "type": "bulleted_list_item",
    #                     "bulleted_list_item": {
    #                         "rich_text": [{
    #                             "type": "text",
    #                             "text": {"content": "Access count: "},
    #                             "annotations": {"bold": True}
    #                         }, {
    #                             "type": "text",
    #                             "text": {"content": ACCESS_COUNTS[0]},
    #                             "annotations": {"color": "orange"}
    #                         }]}
    #                 }, {
    #                     "object": BLOCK,
    #                     "type": "image",
    #                     "image": {
    #                         "type": "external",
    #                         "external": {
    #                             "url": (
    #                                 f"{df_banners['banner'].unique()[1]}")}
    #                         }},
    #                 {
    #                     "object": BLOCK,
    #                     "type": "bulleted_list_item",
    #                     "bulleted_list_item": {
    #                         "rich_text": [{
    #                             "type": "text",
    #                             "text": {"content": "Request Type: "},
    #                             "annotations": {"bold": True}
    #                         }, {
    #                             "type": "text",
    #                             "text": {"content": "FAQ"},
    #                             "annotations": {"color": "orange"}
    #                         }]}
    #                 }, {
    #                     "object": BLOCK,
    #                     "type": "bulleted_list_item",
    #                     "bulleted_list_item": {
    #                         "rich_text": [{
    #                             "type": "text",
    #                             "text": {"content": "Access count: "},
    #                             "annotations": {"bold": True}
    #                         }, {
    #                             "type": "text",
    #                             "text": {"content": ACCESS_COUNTS[1]},
    #                             "annotations": {"color": "orange"}
    #                         }]}
    #                 }, {
    #                     "object": BLOCK,
    #                     "type": "image",
    #                     "image": {
    #                         "type": "external",
    #                         "external": {
    #                             "url": (
    #                                 f"{df_banners['banner'].unique()[2]}")}
    #                         }},
    #                 {
    #                     "object": BLOCK,
    #                     "type": "bulleted_list_item",
    #                     "bulleted_list_item": {
    #                         "rich_text": [{
    #                             "type": "text",
    #                             "text": {"content": "Request Type: "},
    #                             "annotations": {"bold": True}
    #                         }, {
    #                             "type": "text",
    #                             "text": {"content": "Room Service"},
    #                             "annotations": {"color": "orange"}
    #                         }]}
    #                 }, {
    #                     "object": BLOCK,
    #                     "type": "bulleted_list_item",
    #                     "bulleted_list_item": {
    #                         "rich_text": [{
    #                             "type": "text",
    #                             "text": {"content": "Access count: "},
    #                             "annotations": {"bold": True}
    #                         }, {
    #                             "type": "text",
    #                             "text": {"content": ACCESS_COUNTS[2]},
    #                             "annotations": {"color": "orange"}
    #                         }]}
    #                 }, {
    #                     "object": BLOCK,
    #                     "type": "image",
    #                     "image": {
    #                         "type": "external",
    #                         "external": {
    #                             "url": (
    #                                 f"{df_banners['banner'].unique()[3]}")}
    #                         }},
    #                 {
    #                     "object": BLOCK,
    #                     "type": "bulleted_list_item",
    #                     "bulleted_list_item": {
    #                         "rich_text": [{
    #                             "type": "text",
    #                             "text": {"content": "Request Type: "},
    #                             "annotations": {"bold": True}
    #                         }, {
    #                             "type": "text",
    #                             "text": {"content": "Experience"},
    #                             "annotations": {"color": "orange"}
    #                         }]}
    #                 }, {
    #                     "object": BLOCK,
    #                     "type": "bulleted_list_item",
    #                     "bulleted_list_item": {
    #                         "rich_text": [{
    #                             "type": "text",
    #                             "text": {"content": "Access count: "},
    #                             "annotations": {"bold": True}
    #                         }, {
    #                             "type": "text",
    #                             "text": {"content": ACCESS_COUNTS[3]},
    #                             "annotations": {"color": "orange"}
    #                         }]}
    #                 }, {
    #                     "object": BLOCK,
    #                     "type": "image",
    #                     "image": {
    #                         "type": "external",
    #                         "external": {
    #                             "url": (
    #                                 f"{df_banners['banner'].unique()[4]}")}
    #                         }},
    #                 {
    #                     "object": BLOCK,
    #                     "type": "bulleted_list_item",
    #                     "bulleted_list_item": {
    #                         "rich_text": [{
    #                             "type": "text",
    #                             "text": {"content": "Request Type: "},
    #                             "annotations": {"bold": True}
    #                         }, {
    #                             "type": "text",
    #                             "text": {"content": "Experience"},
    #                             "annotations": {"color": "orange"}
    #                         }]}
    #                 }, {
    #                     "object": BLOCK,
    #                     "type": "bulleted_list_item",
    #                     "bulleted_list_item": {
    #                         "rich_text": [{
    #                             "type": "text",
    #                             "text": {"content": "Access count: "},
    #                             "annotations": {"bold": True}
    #                         }, {
    #                             "type": "text",
    #                             "text": {"content": ACCESS_COUNTS[4]},
    #                             "annotations": {"color": "orange"}
    #                         }]}
    #                 }, {
    #                     "object": BLOCK,
    #                     "type": "image",
    #                     "image": {
    #                         "type": "external",
    #                         "external": {
    #                             "url": (
    #                                 f"{df_banners['banner'].unique()[5]}")}
    #                         }},
    #                 {
    #                     "object": BLOCK,
    #                     "type": "bulleted_list_item",
    #                     "bulleted_list_item": {
    #                         "rich_text": [{
    #                             "type": "text",
    #                             "text": {"content": "Request Type: "},
    #                             "annotations": {"bold": True}
    #                         }, {
    #                             "type": "text",
    #                             "text": {"content": "FAQ"},
    #                             "annotations": {"color": "orange"}
    #                         }]}
    #                 }, {
    #                     "object": BLOCK,
    #                     "type": "bulleted_list_item",
    #                     "bulleted_list_item": {
    #                         "rich_text": [{
    #                             "type": "text",
    #                             "text": {"content": "Access count: "},
    #                             "annotations": {"bold": True}
    #                         }, {
    #                             "type": "text",
    #                             "text": {"content": ACCESS_COUNTS[5]},
    #                             "annotations": {"color": "orange"}
    #                         }]}
    #                 }, {
    #                     "object": BLOCK,
    #                     "type": "image",
    #                     "image": {
    #                         "type": "external",
    #                         "external": {
    #                             "url": (
    #                                 f"{df_banners['banner'].unique()[6]}")}
    #                         }},
    #                 {
    #                     "object": BLOCK,
    #                     "type": "bulleted_list_item",
    #                     "bulleted_list_item": {
    #                         "rich_text": [{
    #                             "type": "text",
    #                             "text": {"content": "Request Type: "},
    #                             "annotations": {"bold": True}
    #                         }, {
    #                             "type": "text",
    #                             "text": {"content": "Experience"},
    #                             "annotations": {"color": "orange"}
    #                         }]}
    #                 }, {
    #                     "object": BLOCK,
    #                     "type": "bulleted_list_item",
    #                     "bulleted_list_item": {
    #                         "rich_text": [{
    #                             "type": "text",
    #                             "text": {"content": "Access count: "},
    #                             "annotations": {"bold": True}
    #                         }, {
    #                             "type": "text",
    #                             "text": {"content": ACCESS_COUNTS[6]},
    #                             "annotations": {"color": "orange"}
    #                         }]}
    #                 },]
    #         }}, {
    #         "object": BLOCK,
    #         "heading_1": {
    #             "rich_text": [{
    #                 "text": {"content": CHAPTER_10}}]}
    #         }, {
    #         "object": BLOCK,
    #         "type": "paragraph",
    #         "paragraph": {
    #             "rich_text": [{
    #                 "text": {"content": CHAPTER_10_INTRO}}]}
    #         }]
    # }

    # create_response = requests.post(
    #     "https://api.notion.com/v1/pages",
    #     json=create_page_body,
    #     headers=headers,
    #     timeout=5000)

    # print(create_response.json())
