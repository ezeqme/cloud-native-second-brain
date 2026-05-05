---
type: promcon-talk
conference: PromCon
edition: "PromCon Online 2020"
edition_id: 2020-online
year: 2020
city: "Online"
country: "Online"
topics: ["Prometheus Core", "Remote Write Storage", "Scalability Reliability"]
speakers: []
source_url: https://promcon.io/2020-online/talks/the-future-of-prometheus-and-its-ecosystem/
youtube_url: https://www.youtube.com/watch?v=N8jf1E0XXPY
youtube_search_url: https://www.youtube.com/results?search_query=The+Future+of+Prometheus+and+its+Ecosystem+PromCon+2020
video_match_score: 0.757
status: video-found
---

# The Future of Prometheus and its Ecosystem

## Identificação

- Edição: PromCon Online 2020
- País/cidade: Online / Online
- Temas: [[Prometheus Core]], [[Remote Write Storage]], [[Scalability Reliability]]
- Speakers: N/A
- Página oficial: https://promcon.io/2020-online/talks/the-future-of-prometheus-and-its-ecosystem/
- YouTube: https://www.youtube.com/watch?v=N8jf1E0XXPY

## Resumo

Speaker: Richard "RichiH" Hartmann Prometheus has taken the world by storm and continues to make inroads into new fields. We will be talking about the near and long-term future of Prometheus, and how it will continue to shape the ecosystem around itself.

## Abstract oficial

Speaker: Richard "RichiH" Hartmann

Prometheus has taken the world by storm and continues to make inroads into new fields. We will be talking about the near and long-term future of Prometheus, and how it will continue to shape the ecosystem around itself.

## Links

- Página oficial: https://promcon.io/2020-online/talks/the-future-of-prometheus-and-its-ecosystem/
- YouTube: https://www.youtube.com/watch?v=N8jf1E0XXPY
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=N8jf1E0XXPY
- YouTube title: PromCon Online 2020 - The Future of Prometheus and its Ecosystem Richard Hartmann @ Grafana Labs
- Match score: 0.757
- Transcript file: _sources/transcripts/youtube-enriched/promcon/2020/the-future-of-prometheus-and-its-ecosystem/N8jf1E0XXPY.txt
- Transcript chars: 36279
- Keywords: actually, prometheus, consensus, documentation, probably, basically, within, already, environment, person, obviously, summit, discussion, course, easier, support, little, document

### Resumo baseado na transcript

[Music] hey all right welcome back uh we're now going to hear from richie h about the future of the prometheus in the ecosystem brian roll the clip yeah does actually me we're doing this live [Laughter] um so yeah oh no live oh yes let's see if that one works so welcome to the future of prometheus let's start with a quick recap of what happened since since the last program for 2.14 the highlight feature was definitely the react ui it's still experimental and it hasn't reached feature

### Excerpt da transcript

[Music] hey all right welcome back uh we're now going to hear from richie h about the future of the prometheus in the ecosystem brian roll the clip yeah does actually me we're doing this live [Laughter] um so yeah oh no live oh yes let's see if that one works so welcome to the future of prometheus let's start with a quick recap of what happened since since the last program for 2.14 the highlight feature was definitely the react ui it's still experimental and it hasn't reached feature parity yet but it's slowly getting there and if you have a promises which is 2.14 or new which you should have you'll find a small thing in the upper right which lets you try the new based ui and it's super nice for 2.15 we have the metadata api we have exposed or supported help type and such information for ages within permissive exposition format but we haven't really done anything with it so now we have an api for externalizing this kind of data and here you can see the graphana explore ui taking taking advantage of this to show the user what they're actually looking at and just giving more context about what they're currently building what they're currently digging down into 2.16 was mostly about improvements and stability if i had to if i had to highlight two things it would probably be time zone support for anyone who's not working in utc you can just set your time zone locally and also there is the query log which is a feature request from 2016 so it's nice to finally have a tick mark next to that one speaking about really old stuff um isolation the eye in isothesis in asic databases and fun fact if you remember that particular slide from from just now from garner stock that's because both him and we stole it from gotham so acetate eats acid stands for atomicity consistency isolation durability and it's super nice to finally have isolation 2.18 was mainly about tracing maximum flowers within prometheus and thus obviously also cortex and thanos and you can now really drill down into into stuff but also you have example support and for those who don't know who don't know german jaeger or jaeger in german means hunter a hunter who's literally looking at traces as to why that hunter is hunting humans i don't know 2.19 ram ram ram memory this is insane going from up to above 30 like 33 down to maybe 16 ish that's 50 optimization and on the one hand it's it's super nice to see that we have that kind of potential within with information still it's also somewhat scary to be hon
