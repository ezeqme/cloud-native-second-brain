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
speakers: ["Andy Beane", "Spotify"]
sched_url: https://kccncna2025.sched.com/event/27FZ2/adopting-a-fleet-first-mindset-andy-beane-spotify
youtube_search_url: https://www.youtube.com/results?search_query=Adopting+a+Fleet-first+Mindset+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Adopting a Fleet-first Mindset - Andy Beane, Spotify

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2025 - Atlanta, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]]
- País/cidade: United States / Atlanta
- Speakers: Andy Beane, Spotify
- Schedule: https://kccncna2025.sched.com/event/27FZ2/adopting-a-fleet-first-mindset-andy-beane-spotify
- Busca YouTube: https://www.youtube.com/results?search_query=Adopting+a+Fleet-first+Mindset+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Adopting a Fleet-first Mindset.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2025.sched.com/event/27FZ2/adopting-a-fleet-first-mindset-andy-beane-spotify
- YouTube search: https://www.youtube.com/results?search_query=Adopting+a+Fleet-first+Mindset+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=-E9ffAB3DoA
- YouTube title: Adopting a Fleet-first Mindset - Andy Beane, Spotify
- Match score: 0.839
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/adopting-a-fleet-first-mindset/-E9ffAB3DoA.txt
- Transcript chars: 29513
- Keywords: change, changes, components, software, fleetwide, management, spotify, version, question, organization, across, course, mindset, approach, impact, migration, making, rolling

### Resumo baseado na transcript

Well, I'm an engineer at Spotify and I work on a team named Starfleet or Squad as we call it internally where we work on a problem area called fleet management and we build a platform called Fleet Shift among some other pretty cool things. Well, first let's talk about the challenges of managing software at scale, at least at Spotify in the past. Maintaining your fleet of software becomes complicated, slow, and a huge cost that outpaces the scale of your organization. Some examples of these types of things, just to name a few, are updating dependencies, migrating to a new service, tool, or framework, uh patching a security vulnerability or resolving a production incident. It could also be an infrastructure change, something that's improving the scalability and performance of your fleet, or even provide a cost savings to the organization. Uh, and these are the things that get in the way between you and the important problems that your you and your teams are trying to solve.

### Excerpt da transcript

Hello, good morning. Uh, thank you everyone for coming. Welcome to adopting a fleet first mindset at Spotify. So, who am I? Why listen to me today? Well, I'm an engineer at Spotify and I work on a team named Starfleet or Squad as we call it internally where we work on a problem area called fleet management and we build a platform called Fleet Shift among some other pretty cool things. So, what are we going to talk about today? Well, first let's talk about the challenges of managing software at scale, at least at Spotify in the past. Next, to talk about our journey of adopting a fleet first mindset, it's first important to talk about the pillars and building blocks we've used to build fleet shift and perform fleetwide changes at scale. Then, I'd like to dive a little deeper into making fleet first changes and what this looks like. After that, I'd like to share what a fleet first mindset is for engineers building and rolling out fleetwide changes and the impact. Last, let's take a look at some real life examples of changes that are ongoing and recurring, some that are in the past, and some ideas that we're looking at as we consider what the future of adopting a fleet first mindset can be at Spotify.

So first when journeying to a fleet first mindset we started to look at our software ecosystem in terms of software components and software components simply put are any type of software entity within your organization. So its backend services its websites its infrastructure and tools its mobile and client features uh its data pipelines and more. Now, with the nearly 20 years that Spotify has been around, the number of software components has overwhelmingly grown larger and faster than the number of engineers in our organization. We have increased complexity, more teams, products, and of course, priorities. This means more maintenance, more migrations, all of which are harder to do with our growing software fleet. So what is some of the engineering impact that all of this has had from all the software that we have written? Well, we have over 3,800 production deployments per day. And we capture over 1.7 trillion events per day, which I don't know about any of you, but numbers like these I I honestly can't even wrap my head around.

1.7 trillion. Uh, and with that, we have over 10 million requests per second of peak daily traffic. at least the way we can best measure it. And so what is the actual impact and what does all of this support and deliver? Well, Spotify
