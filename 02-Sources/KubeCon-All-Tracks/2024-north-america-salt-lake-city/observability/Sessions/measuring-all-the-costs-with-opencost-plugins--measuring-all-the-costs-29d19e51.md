---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Observability"
themes: ["Observability"]
speakers: ["Alex Meijer", "Stackwatch"]
sched_url: https://kccncna2024.sched.com/event/1i7oQ/measuring-all-the-costs-with-opencost-plugins-alex-meijer-stackwatch
youtube_search_url: https://www.youtube.com/results?search_query=Measuring+All+the+Costs+with+OpenCost+Plugins+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Measuring All the Costs with OpenCost Plugins - Alex Meijer, Stackwatch

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Observability]]
- Temas: [[Observability]]
- País/cidade: United States / Salt Lake City
- Speakers: Alex Meijer, Stackwatch
- Schedule: https://kccncna2024.sched.com/event/1i7oQ/measuring-all-the-costs-with-opencost-plugins-alex-meijer-stackwatch
- Busca YouTube: https://www.youtube.com/results?search_query=Measuring+All+the+Costs+with+OpenCost+Plugins+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Measuring All the Costs with OpenCost Plugins.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7oQ/measuring-all-the-costs-with-opencost-plugins-alex-meijer-stackwatch
- YouTube search: https://www.youtube.com/results?search_query=Measuring+All+the+Costs+with+OpenCost+Plugins+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=yLAx2z4FqSk
- YouTube title: Measuring All the Costs with OpenCost Plugins - Alex Meijer, Stackwatch
- Match score: 0.876
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/measuring-all-the-costs-with-opencost-plugins/yLAx2z4FqSk.txt
- Transcript chars: 29039
- Keywords: cost, plugins, plugin, fields, looking, plug-in, trying, basically, interface, little, course, provide, together, contribute, support, providers, organization, provider

### Resumo baseado na transcript

uh welcome thanks for coming uh my name is Alex Meyer and I'm a software engineer at Cube cost but uh here this afternoon in my capacity as an open cost maintainer and a maintainer of the open cost plugins project so was very excited to talk to you about open cost and some really exciting recent developments uh first we'll take a quick look at open cost past where it is today and where we're going at a high level we'll sort then sort of dig into the substance

### Excerpt da transcript

uh welcome thanks for coming uh my name is Alex Meyer and I'm a software engineer at Cube cost but uh here this afternoon in my capacity as an open cost maintainer and a maintainer of the open cost plugins project so was very excited to talk to you about open cost and some really exciting recent developments uh first we'll take a quick look at open cost past where it is today and where we're going at a high level we'll sort then sort of dig into the substance of the presentation which is open cost plugins specifically how we use the focus spec a lot more on that later we'll touch quickly on plug-in functionality and delivery how plugins work and peek under the hood a little bit a demo of course and uh then we'll end the session with with some Road mapping and sort of goal setting here but before we begin uh I couldn't resist the urge to sort of give my uh perspective on kubernetes at 10 years in the spirit of the festivities here I've been working with Kate since early 2017 so you know not there from the beginning but you know I've seen a lot of changes and uh you know my biggest takeaway is that kubernetes really doesn't have to prove itself anymore right and and this is sort of what we're seeing in a lot of the other you know talks and things like that um where you know I don't know about y'all but like for me I'm not getting what is kubernetes so much when I tell people what I work with and what I do and that's awesome right and uh you know various surveys cncf survey that I cited uh is like 89% penetration right most companies at least the ones surveyed or at least evaluating or using Kates in production U and you know because it Daves a lot of companies a lot of money right and it accelerates them um especially in the beginning right I remember the organization that I was with when I first discovered kubernetes right we saw an order of magnitude reduction in our compute cost uh but then what happened well we took the savings and we grew right as an industry and in as individual companies right so I mean come on 10 years ago right we could never imagine the things we're doing here so all of a sudden right we find our apps are getting expensive once more right and I sort of take an opinion here and like this is The Gardener hype cycle right for those of you who aren't familiar with it and uh are we in the trough of disillusionment or some way in or out of that right because all of a sudden these new technologies are costing us a lot of money right uh I
