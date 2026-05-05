---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Platform Engineering"
themes: ["Platform Engineering"]
speakers: ["Bogdan Stancu", "Adobe"]
sched_url: https://kccnceu2026.sched.com/event/2CW7c/freedom-through-boundaries-building-configurations-that-age-well-bogdan-stancu-adobe
youtube_search_url: https://www.youtube.com/results?search_query=Freedom+Through+Boundaries%3A+Building+Configurations+That+Age+Well+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Freedom Through Boundaries: Building Configurations That Age Well - Bogdan Stancu, Adobe

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Platform Engineering]]
- Temas: [[Platform Engineering]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Bogdan Stancu, Adobe
- Schedule: https://kccnceu2026.sched.com/event/2CW7c/freedom-through-boundaries-building-configurations-that-age-well-bogdan-stancu-adobe
- Busca YouTube: https://www.youtube.com/results?search_query=Freedom+Through+Boundaries%3A+Building+Configurations+That+Age+Well+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Freedom Through Boundaries: Building Configurations That Age Well.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2CW7c/freedom-through-boundaries-building-configurations-that-age-well-bogdan-stancu-adobe
- YouTube search: https://www.youtube.com/results?search_query=Freedom+Through+Boundaries%3A+Building+Configurations+That+Age+Well+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=H1g0jnmjJN8
- YouTube title: Freedom Through Boundaries: Building Configurations That Age Well - Bogdan Stancu, Adobe
- Match score: 0.945
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/freedom-through-boundaries-building-configurations-that-age-well/H1g0jnmjJN8.txt
- Transcript chars: 21657
- Keywords: change, configuration, config, anything, secrets, boundaries, pretty, another, whenever, product, provide, breaking, default, management, whatever, outcome, shouldn, better

### Resumo baseado na transcript

And today we're going to talk about building configurations that age well. Uh I would first like to ask who in this room does this does uh configuration management for other users. I guess most of you already know what Helm is because uh this is going to be uh based on a Helm chart and yeah well Helm templating for for Kubernetes. We have a global field which is going to change all three sets of collectors and then one for metrics, one for traces, one for logs. Think that you have too few tests because if it takes 5 minutes more to merge a PR, it's never a problem. However, there is one fundamental reason why people don't follow these practices and it is that there is cost to them.

### Excerpt da transcript

Hello everyone. I'm Bogdan. I work for Adobe in the observability team. And today we're going to talk about building configurations that age well. Uh I would first like to ask who in this room does this does uh configuration management for other users. Can you Yeah. Oh, a lot of people. That's great. Yeah. Uh just so you know this talk is uh we'll present a case that is a bit extreme and most of us when we think about what I'm going to present will think that everything is pretty normal like you you think about what we're going to talk about but if you don't actively keep thinking about the rules that we're going to present uh things can kind of shift now one of the questions I guess you all have is who's a dog and he's my dog. He's 3 years old. I have no creativity. He's a terrier. So, his name is Terry. And we've been training for 3 years almost. Like right as I got him, we started training. And I constantly keep hearing people telling me that he's just a dog and I shouldn't train him. He should be free to do whatever he wants because it's better for him.

But that's not really the case. And I found out that whenever I go in the park, for example, everybody has their dog on a leash, but Terry can be free because I set some boundaries. I set some rules and I know that he's going to come back whenever I call him. We go on hikes. I feel like he has a lot more freedom because I set up some boundaries. And this thing made me uh realize that it's kind of the same thing with user management, kind of configuration management. You have to put rules so the users are more free. They cannot really break stuff. They can't really go wrong. Some prerequisites. I guess most of you already know what Helm is because uh this is going to be uh based on a Helm chart and yeah well Helm templating for for Kubernetes. You give it a template which is the top part with that values uh thing. You give a values file and then it spits out uh the combined configuration. What what's important here is that what we will talk about the API is the config file the that you can't see it uh the thing on the bottom that's that's what users see that's what they should care about.

Then again, uh, open telemetry. I guess you all heard a lot of open telemetry this week. Uh, so I'm not going to go really into what the collector is, but it's an agent. It has a configuration, and this is what uh, our well example will spit out. Okay. Now, we're going to imagine that we are an observability team buil
