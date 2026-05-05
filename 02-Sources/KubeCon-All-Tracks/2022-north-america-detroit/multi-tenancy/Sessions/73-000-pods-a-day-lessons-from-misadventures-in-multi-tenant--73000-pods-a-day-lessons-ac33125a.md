---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Multi-tenancy"
themes: ["Multi-tenancy"]
speakers: ["Shane Corbett", "Amazon Web Services", "Wil Reed", "Acquia"]
sched_url: https://kccncna2022.sched.com/event/182D5/73000-pods-a-day-lessons-from-misadventures-in-multi-tenant-shane-corbett-amazon-web-services-wil-reed-acquia
youtube_search_url: https://www.youtube.com/results?search_query=73%2C000+Pods+a+Day%2C+Lessons+From+Misadventures+In+Multi-Tenant+CNCF+KubeCon+2022
slides: []
status: parsed
---

# 73,000 Pods a Day, Lessons From Misadventures In Multi-Tenant - Shane Corbett, Amazon Web Services & Wil Reed, Acquia

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Multi-tenancy]]
- Temas: [[Multi-tenancy]]
- País/cidade: United States / Detroit
- Speakers: Shane Corbett, Amazon Web Services, Wil Reed, Acquia
- Schedule: https://kccncna2022.sched.com/event/182D5/73000-pods-a-day-lessons-from-misadventures-in-multi-tenant-shane-corbett-amazon-web-services-wil-reed-acquia
- Busca YouTube: https://www.youtube.com/results?search_query=73%2C000+Pods+a+Day%2C+Lessons+From+Misadventures+In+Multi-Tenant+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre 73,000 Pods a Day, Lessons From Misadventures In Multi-Tenant.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182D5/73000-pods-a-day-lessons-from-misadventures-in-multi-tenant-shane-corbett-amazon-web-services-wil-reed-acquia
- YouTube search: https://www.youtube.com/results?search_query=73%2C000+Pods+a+Day%2C+Lessons+From+Misadventures+In+Multi-Tenant+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=NqtfDy_KAqg
- YouTube title: 73,000 Pods a Day, Lessons From Misadventures In Multi-Tenant - Shane Corbett & Wil Reed
- Match score: 0.919
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/73-000-pods-a-day-lessons-from-misadventures-in-multi-tenant/NqtfDy_KAqg.txt
- Transcript chars: 33048
- Keywords: second, requests, little, actually, container, percent, application, running, performance, thinking, number, threads, seconds, request, milliseconds, metric, pretty, amount

### Resumo baseado na transcript

gang thanks for coming today uh we've got a packed agenda I think we're clocked in at like 34 30. so we're going to start right at the pen uh we can't take any questions to get through all of it but I tell you what we will stay as long as it takes to answer all your questions um so don't think that we're

### Excerpt da transcript

gang thanks for coming today uh we've got a packed agenda I think we're clocked in at like 34 30. so we're going to start right at the pen uh we can't take any questions to get through all of it but I tell you what we will stay as long as it takes to answer all your questions um so don't think that we're fleeing the scene or anything like that I promise we'll be with you um and I think we're about two minutes out thank you very much for coming in if you guys in the back it's not like the Blue Man Group we won't spread anything on here or anything so feel free plenty of places up front thanks again foreign take a picture for me yeah oh I turned my turn my phone off so let's begin drink called the kubecon police on you all right all right that's good to go I'm good sorry ladies and gentlemen my name's Shane this is my good friend will and this whole week at kubecon you're going to hear amazing success story after amazing success story delivered by some of the most brilliant people in our industry so will and I we're going to give you a break from all that right now we're going to tell you about a misadventure we had running a large-scale kubernetes cluster and the reason why we think you're going to be interested in this is We Believe that many of you in this room right now are on this misadventure with us it's just no one told you our misadventure begins we're all great misadventure begins a misunderstanding you see we took the things that we knew to be true in kubernetes and misapplied all those Concepts to things that were actually governed by the Linux performance rules and it turns out that's kind of a big mistake to make but it's an easy one to make you see we were thinking in cores because that's how kubernetes thinks about stuff right there is a node object with the number of CPUs on it and every time you schedule something it decrements that object it's definitely a thing however Linux has an abstraction layer and it thinks in time not cores now I get it I'm probably sounding like the crazy guy on the kubernetes subway right the chords are a lot so let me explain that for just a second okay so I'm going to use the least controversial feature in all of kubernetes to explain this kubernetes limits now I know I know right there's there's a little take how you feel about kubernetes limits and put that aside for me for just a second because it is the best way to understand how kubernetes thinks in time and how dangerous it can be to think in cores just a
