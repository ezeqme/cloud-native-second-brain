---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Platform Engineering"
themes: ["Platform Engineering", "Kubernetes Core"]
speakers: ["Nick Young", "Isovalent at Cisco"]
sched_url: https://kccnceu2025.sched.com/event/1tx7B/dont-write-controllers-like-charlie-dont-does-avoiding-common-kubernetes-controller-mistakes-nick-young-isovalent-at-cisco
youtube_search_url: https://www.youtube.com/results?search_query=Don%27t+Write+Controllers+Like+Charlie+Don%27t+Does%3A+Avoiding+Common+Kubernetes+Controller+Mistakes+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Don't Write Controllers Like Charlie Don't Does: Avoiding Common Kubernetes Controller Mistakes - Nick Young, Isovalent at Cisco

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]], [[Kubernetes Core]]
- País/cidade: United Kingdom / London
- Speakers: Nick Young, Isovalent at Cisco
- Schedule: https://kccnceu2025.sched.com/event/1tx7B/dont-write-controllers-like-charlie-dont-does-avoiding-common-kubernetes-controller-mistakes-nick-young-isovalent-at-cisco
- Busca YouTube: https://www.youtube.com/results?search_query=Don%27t+Write+Controllers+Like+Charlie+Don%27t+Does%3A+Avoiding+Common+Kubernetes+Controller+Mistakes+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Don't Write Controllers Like Charlie Don't Does: Avoiding Common Kubernetes Controller Mistakes.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tx7B/dont-write-controllers-like-charlie-dont-does-avoiding-common-kubernetes-controller-mistakes-nick-young-isovalent-at-cisco
- YouTube search: https://www.youtube.com/results?search_query=Don%27t+Write+Controllers+Like+Charlie+Don%27t+Does%3A+Avoiding+Common+Kubernetes+Controller+Mistakes+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=tnSraS9JqZ8
- YouTube title: Don't Write Controllers Like Charlie Don't Does: Avoiding Common Kubernetes Controller... Nick Young
- Match score: 1.005
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/dont-write-controllers-like-charlie-dont-does-avoiding-common-kubernet/tnSraS9JqZ8.txt
- Transcript chars: 34274
- Keywords: controller, object, gateway, reconcile, objects, changes, function, actually, update, updates, charlie, client, server, selium, controllers, reconciling, runtime, routes

### Resumo baseado na transcript

And I'm here to talk to you today about writing controllers and how it's a bit trickier than you might think. Um, well, yeah, like I said, I'm Nick Young, but uh, I started looking into CDs in early 2017 when they were still called third party resources. So yeah, take a moment to feel sorry for Charlie, but we're all going to learn from his mistakes today. The the mirror of that problem is every time you do an update, you post the whole object back to the API server and the API server has to take that object uh check it all for uh storage versions and stuff and then push it back down to ATD. Um but also once you do that it now means you have a cation validation problem like yay you know like I always like to say there's two hard problems in computer science naming things cation validation and off by one errors right so um the uh you know cation validation is a really hard problem so it makes sense to try and make it not your problem um but the most important thing here that even no matter what framework you're choosing is to limit the number of API

### Excerpt da transcript

Hi everyone. Uh, welcome to don't write controllers like Charlie Don't does. Uh, I am Nick Young from isalen at Cisco. Uh, yeah. And I'm here to talk to you today about writing controllers and how it's a bit trickier than you might think. Okay, so first up, who am I to talk about this? Um, well, yeah, like I said, I'm Nick Young, but uh, I started looking into CDs in early 2017 when they were still called third party resources. Um, I was involved in building out uh Contour's HTTP proxy C that replaced its ingress route C. So I've done a couple of like real life redesigns. Uh, and I've been involved in gateway API since its inception of 2018. Um, which is delivered purely using C. So I've done lots of C stuff. Uh, I've done lots of C design. Uh, and most importantly, uh, I built lots of controllers to do the same thing and I've screwed it up plenty of times, right? So don't feel bad if you screw this stuff up. It's actually surprisingly difficult. Okay, so today's agenda, we're going to walk through some uh CRD controller any patterns using Charlie don't as our straw man.

You can see from the name I chose the names. So it's got CRD in it. Um but yeah, I want to give you some tips on how to avoid them, how not to make the mistakes I have. Um have a look at some of the frameworks available that make some of this stuff a lot easier. Uh and give you some tips about what not to do with them. Again, based on stuff that I have done. Okay, so why Charlie don't? Well, you can thank The Simpsons for that. Um, so, uh, I love The Simpsons. Uh, this particular episode was Bark Got a Knife, and they gave him this helpful book with, uh, Don't Do What Donny Don't Does. Uh, and so, uh, yeah, so I was trying to figure a way to make this sort of stuff a little bit less dry, a little bit more fun. Uh, and so, yeah, I came up with Charlie Don't. Uh, Charlie works on a custom controller for Kubernetes, a big co. Uh, yeah, he just always manages to make the wrong decision and like and mess himself up. So yeah, take a moment to feel sorry for Charlie, but we're all going to learn from his mistakes today.

So thank you. Now, so uh I've done two talks uh using Charlie before. The first one was about designing CDs. That uh QR code will take you to the to the YouTube uh for that talk. That was a reax. Um, so these are the tips I, you know, stuff like reading the API bibles, uh, thinking about how your users will use the CD, using status, you know, avoiding certain types of, uh, value
