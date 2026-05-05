---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2025 - Atlanta, United States"
event_id: kccncna2025
year: 2025
region: "North America"
city: "Atlanta"
country: "United States"
event_date: "2025-11-10/2025-11-13"
track: "Platform Engineering"
themes: ["Platform Engineering"]
speakers: ["Mathieu Girard", "Teddy Poingt", "Beneva"]
sched_url: https://kccncna2025.sched.com/event/27Fcu/the-journey-of-deploying-backstage-in-a-large-organization-mathieu-girard-teddy-poingt-beneva
youtube_search_url: https://www.youtube.com/results?search_query=The+Journey+of+Deploying+Backstage+in+a+Large+Organization+CNCF+KubeCon+2025
slides: []
status: parsed
---

# The Journey of Deploying Backstage in a Large Organization - Mathieu Girard & Teddy Poingt, Beneva

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]]
- País/cidade: United States / Atlanta
- Speakers: Mathieu Girard, Teddy Poingt, Beneva
- Schedule: https://kccncna2025.sched.com/event/27Fcu/the-journey-of-deploying-backstage-in-a-large-organization-mathieu-girard-teddy-poingt-beneva
- Busca YouTube: https://www.youtube.com/results?search_query=The+Journey+of+Deploying+Backstage+in+a+Large+Organization+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre The Journey of Deploying Backstage in a Large Organization.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Fcu/the-journey-of-deploying-backstage-in-a-large-organization-mathieu-girard-teddy-poingt-beneva
- YouTube search: https://www.youtube.com/results?search_query=The+Journey+of+Deploying+Backstage+in+a+Large+Organization+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=l7OQdrUkoVI
- YouTube title: The Journey of Deploying Backstage in a Large Organization - Mathieu Girard & Teddy Poingt, Beneva
- Match score: 0.848
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/the-journey-of-deploying-backstage-in-a-large-organization/l7OQdrUkoVI.txt
- Transcript chars: 29544
- Keywords: portal, integration, backstage, developer, actually, developers, product, company, catalog, plug-in, leadership, documentation, repository, github, understand, component, useful, access

### Resumo baseado na transcript

Uh, just before we get started, raise your hand if you have backstage running in production right now. So, I hope you guys will be able to relate to what we're about to say and for the rest of you, let's hope we'll help you get there. I mean doing tool selections, learning new things, experimentation and all of this is of course not a lot of value creations for the company. stuff and all that automate uh the more that we could of course and optimize performance and quality and stuff like that. So, of course, we talked a lot about the problem with the developer experience. This DevX state that we had uh all this cognitive load problem that our developer had that they had all day long.

### Excerpt da transcript

Uh, welcome everybody. Thank you for being here. Uh, we know it's been a long week here at CubeCon. So, it's 11 o'clock on the last day of the conference. Thank you very much for being here. We'll do our best to be interesting until the end. So, the journey of deploying backstage in a large organization. Uh, just before we get started, raise your hand if you have backstage running in production right now. Okay, good. And keep it up if you are working in a large organizations. let's say a thousand employees or more. All right, good. So, I hope you guys will be able to relate to what we're about to say and for the rest of you, let's hope we'll help you get there. So, uh before we start who we are, my name is Matsujiar. I've been a developer and a software architect for a long time and I'm software engineering manager at Ben for a couple years now. >> And hi everyone, my name is Tedipor. I'm a software architect and I'm in charge of all the developer tools in Benova's IT platform. >> Thank you, Teddy. And what is Benva?

Uh I'm guessing probably most of you never heard of Benva before. We are actually based in Canada. Uh largest mutual insurance company out in Canada and also one of the largest in the overall Canadian insurance market. uh over $27 billion in assets, uh more than 3.5 million customers or clients, and uh to this day probably more than 6,000 employees. So, fairly large company, I'd say. Uh 80 years in the making. We're a young company with a lot of history. This liner actually comes from our corporate website. And uh it has a lot more to do with what we're about to talk than you could imagine because uh Benva, you need to know that it's a merger that we've been born in 2020. Uh before that we were two uh older companies in Canada called SSQ and La Capital. And as you could imagine when you merge two large companies like that from an IT point of view uh you actually get a lot of well double of everything at first right uh many many languages many applications many teams working on stuff and trying to integrate into this new company and and of course at this point we were also uh well dealing with this other world even you might have heard about called COVID you know everybody working from home and out.

So uh I guess we could say that at first there was a lot of chaos going on. Uh we were trying to to help our development teams uh work better do the stuff the more the same way uh alto together and I just put right here a very small subset of all
