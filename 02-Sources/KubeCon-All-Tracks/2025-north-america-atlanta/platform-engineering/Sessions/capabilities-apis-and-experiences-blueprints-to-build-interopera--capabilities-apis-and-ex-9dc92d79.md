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
speakers: ["Kyle Penfound", "Dagger", "Mauricio \"Salaboy\" Salatino", "Diagrid"]
sched_url: https://kccncna2025.sched.com/event/27Faa/capabilities-apis-and-experiences-blueprints-to-build-interoperable-platforms-kyle-penfound-dagger-mauricio-salaboy-salatino-diagrid
youtube_search_url: https://www.youtube.com/results?search_query=Capabilities%2C+APIs%2C+and+Experiences%3A+Blueprints+To+Build+Interoperable+Platforms+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Capabilities, APIs, and Experiences: Blueprints To Build Interoperable Platforms - Kyle Penfound, Dagger & Mauricio "Salaboy" Salatino, Diagrid

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]]
- País/cidade: United States / Atlanta
- Speakers: Kyle Penfound, Dagger, Mauricio "Salaboy" Salatino, Diagrid
- Schedule: https://kccncna2025.sched.com/event/27Faa/capabilities-apis-and-experiences-blueprints-to-build-interoperable-platforms-kyle-penfound-dagger-mauricio-salaboy-salatino-diagrid
- Busca YouTube: https://www.youtube.com/results?search_query=Capabilities%2C+APIs%2C+and+Experiences%3A+Blueprints+To+Build+Interoperable+Platforms+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Capabilities, APIs, and Experiences: Blueprints To Build Interoperable Platforms.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27Faa/capabilities-apis-and-experiences-blueprints-to-build-interoperable-platforms-kyle-penfound-dagger-mauricio-salaboy-salatino-diagrid
- YouTube search: https://www.youtube.com/results?search_query=Capabilities%2C+APIs%2C+and+Experiences%3A+Blueprints+To+Build+Interoperable+Platforms+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=tvgMu1yTo20
- YouTube title: Capabilities, APIs, and Experiences: Blueprints To Bu... Kyle Penfound & Mauricio "Salaboy" Salatino
- Match score: 0.787
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/capabilities-apis-and-experiences-blueprints-to-build-interoperable-pl/tvgMu1yTo20.txt
- Transcript chars: 26098
- Keywords: platform, actually, dagger, components, capabilities, builder, platforms, modular, interface, interfaces, install, argo, component, common, unified, manage, within, secret

### Resumo baseado na transcript

So, we're here to talk about uh capabilities, APIs, and experiences uh blueprints to build interoperable platforms. And really what that means is uh finding ways to make modular platforms. Um, and it's always in like a slightly different context whether it's meant to like wow you or scare you or whatever, but like the fact that we have Kubernetes as this unified API on top of our cloud infrastructure is the only reason that this thing even exists. And like it it's really hard to to appreciate the scale of this and like the amount of work that goes into every single one of the tiles up there. So if you look at like all the pods running in Kubernetes like do you know off the top of your head like how one individual application is installed, managed, upgraded. And so all of these problems lead to reduced iteration speed because it's really hard to manage this platform.

### Excerpt da transcript

Awesome. So, we're here to talk about uh capabilities, APIs, and experiences uh blueprints to build interoperable platforms. And really what that means is uh finding ways to make modular platforms. So, we'll dig into uh what that means, why it's hard, and how we can actually make that easier. Uh so, originally, this was meant to be presented by my good friends Marcos and Mauricio. Unfortunately, neither of them could make it today. So, I'm here in their place. I'm Kyle. You can boo me now. Just get it out of the way. Uh if you have any tomatoes, thank you. Um yeah, I'm Kyle. I'm from Dagger. Um Dagger doesn't have anything to do with building module plat modular platforms, but uh it's something that I am interested in and I I work on as well. Um so I've been at Dagger a bit but over three years, but my background is like uh release engineering, DevOps, cloud infra, all that stuff. Um and all the stuff that's led us to where we are where we are today. um which is really the 10 years of Kubernetes. So that's kind of the theme this year is uh we've had 10 years of this.

It's unified the underlying APIs for our cloud infrastructure that's let let us build this crazy ecosystem that we all experience today. Um so it wouldn't be a CubeCon talk if we didn't pull this up, right? So there's the landscape. I think almost every talk we're probably like required to pull it up or something. Um, and it's always in like a slightly different context whether it's meant to like wow you or scare you or whatever, but like the fact that we have Kubernetes as this unified API on top of our cloud infrastructure is the only reason that this thing even exists. And like it it's really hard to to appreciate the scale of this and like the amount of work that goes into every single one of the tiles up there. U so it's really a great time right now to be a platform builder because we have all of these great tools to use. Um, and some of us here at CubeCon, we can get our CNCF shopping cart and walk down the aisles and pick off, you know, a tool from each shelf and build our platform and that's awesome.

But the truth is that for most people, and I don't think this is a secret, for most people looking at this, it's overwhelming, right? Uh, you can't just look at something and know right away. Is is this tool a good choice for my platform? Um, what happens if I make the wrong choice? Like how how do I build the right platform for my users? So that's what we're going to be talking about l
