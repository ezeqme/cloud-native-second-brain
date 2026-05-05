---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Cloud Native Experience"
themes: ["Networking"]
speakers: ["Christian Posta", "Louis Ryan", "Solo.io"]
sched_url: https://kccncna2024.sched.com/event/1i7nP/what-istio-got-wrong-learnings-from-the-last-seven-years-of-service-mesh-christian-posta-louis-ryan-soloio
youtube_search_url: https://www.youtube.com/results?search_query=What+Istio+Got+Wrong%3A+Learnings+from+the+Last+Seven+Years+of+Service+Mesh+CNCF+KubeCon+2024
slides: []
status: parsed
---

# What Istio Got Wrong: Learnings from the Last Seven Years of Service Mesh - Christian Posta & Louis Ryan, Solo.io

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Cloud Native Experience]]
- Temas: [[Networking]]
- País/cidade: United States / Salt Lake City
- Speakers: Christian Posta, Louis Ryan, Solo.io
- Schedule: https://kccncna2024.sched.com/event/1i7nP/what-istio-got-wrong-learnings-from-the-last-seven-years-of-service-mesh-christian-posta-louis-ryan-soloio
- Busca YouTube: https://www.youtube.com/results?search_query=What+Istio+Got+Wrong%3A+Learnings+from+the+Last+Seven+Years+of+Service+Mesh+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre What Istio Got Wrong: Learnings from the Last Seven Years of Service Mesh.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1i7nP/what-istio-got-wrong-learnings-from-the-last-seven-years-of-service-mesh-christian-posta-louis-ryan-soloio
- YouTube search: https://www.youtube.com/results?search_query=What+Istio+Got+Wrong%3A+Learnings+from+the+Last+Seven+Years+of+Service+Mesh+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=XW10IpsTmH8
- YouTube title: What Istio Got Wrong: Learnings from the Last Seven Years of Service Mesh - C. Posta, L. Ryan
- Match score: 0.986
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/what-istio-got-wrong-learnings-from-the-last-seven-years-of-service-me/XW10IpsTmH8.txt
- Transcript chars: 32501
- Keywords: microservices, probably, ambient, google, actually, mesh, software, source, little, getting, involved, vision, deliver, pretty, complexity, policy, absolutely, working

### Resumo baseado na transcript

thank you all for coming out this nice packed room I guess people want to hear about failure and how things went wrong that's more exciting uh so let's uh let's get to it but before we do I'm just kind of curious how many people in the room uh use esto today can you raise your hands if you use ISO today um all right leave your hands raised how many people have used ISO for longer than a year longer than two years all right longer than three so one the key learnings you know if you're going to do a 1.0 1.0 signals ready for production you know a nice marketing event get people come look at it and try to get positive experiences um know who your end user is know but the intent is absolutely to ship that so I don't think it's a mistake in that respect it may absolutely be a mistake that it was a timing problem I don't know like I will continue to make mistakes and that may absolutely be

### Excerpt da transcript

thank you all for coming out this nice packed room I guess people want to hear about failure and how things went wrong that's more exciting uh so let's uh let's get to it but before we do I'm just kind of curious how many people in the room uh use esto today can you raise your hands if you use ISO today um all right leave your hands raised how many people have used ISO for longer than a year longer than two years all right longer than three years four wow all right five wow okay six really there's still a couple people oh my goodness seven oh wow all right all right Vertical Limit well some of the you can put your hands down there yeah um some of this pain that we talk about today is is going to resonate with you I guess um so we're going to talk about some of the things that we learned in the project over the last seven years or seven and a half years now um and uh and I think it'll be useful just to see how you know what what are the criteria that you look for when you adopt an open source project or if there are people who are involved in open source maybe the some of those learnings will be useful for uh for your projects as well um so first we'll introduce ourselves I'll let Lou start here uh hi everyone I'm I'm Lou Ryan uh I've been involved D in the sto project since the very beginning so I'm responsible for a lot of this train wreck narrative that we're about to go through so apologies in retrospect in advance and uh thank you for being here and Lasting through a lot of that yes absolutely um and I'm Christian Posta the global field CTO at uh at solo I've been working on sto since January 2017 I got introduced to shiram who was at IBM at the time uh started uh digging around and and really got interested in it um I followed it I've written some books on this topic i' followed it over the last seven and a half years working with customers experiencing some of this pain myself with with h with our customers and we Lou and I both work at solo um we are uh some of the lead contributors to the SEO project you might recognize some of the names on this uh on this slide um we are driving the uh the future road map for the project um and so a lot of stuff that we've learned we want to bring back and and make the project is uh as good as we can possibly make it so this is approximately what the agenda will look like we'll set some context we'll go into some of the Gory details and then talk a little bit about uh about what we're doing going forward all right
