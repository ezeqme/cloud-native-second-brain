---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Application Development"
themes: ["Security"]
speakers: ["Vish Abrams", "Heroku"]
sched_url: https://kccnceu2025.sched.com/event/1txEa/workload-identity-for-humans-a-twelve-factor-approach-vish-abrams-heroku
youtube_search_url: https://www.youtube.com/results?search_query=Workload+Identity+for+Humans%3A+A+Twelve-Factor+Approach+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Workload Identity for Humans: A Twelve-Factor Approach - Vish Abrams, Heroku

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Application Development]]
- Temas: [[Security]]
- País/cidade: United Kingdom / London
- Speakers: Vish Abrams, Heroku
- Schedule: https://kccnceu2025.sched.com/event/1txEa/workload-identity-for-humans-a-twelve-factor-approach-vish-abrams-heroku
- Busca YouTube: https://www.youtube.com/results?search_query=Workload+Identity+for+Humans%3A+A+Twelve-Factor+Approach+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Workload Identity for Humans: A Twelve-Factor Approach.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txEa/workload-identity-for-humans-a-twelve-factor-approach-vish-abrams-heroku
- YouTube search: https://www.youtube.com/results?search_query=Workload+Identity+for+Humans%3A+A+Twelve-Factor+Approach+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=dNb1m84Bp4c
- YouTube title: Workload Identity for Humans: A Twelve-Factor Approach - Vish Abrams, Heroku
- Match score: 0.928
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/workload-identity-for-humans-a-twelve-factor-approach/dNb1m84Bp4c.txt
- Transcript chars: 28286
- Keywords: application, platform, identity, factor, backend, credentials, request, workload, little, credential, actually, environment, trying, client, developer, support, across, header

### Resumo baseado na transcript

I'm here to talk to you today about workload identity for humans, a 12-factor approach. I'm the chief architect at Heroku and I'm excited to talk about workload identity. But when it comes to workload identity and the reason that we need it is because there's a problem when we start talking about secrets. to worry about these other problems of keeping it in sync and being vulnerable for a long time as that rotation goes through. I've heard stories of companies with hundreds or thousands of microservices that have a large credential leak where they have to rotate all of their applications at once or over a period of multiple weeks and during that intervening time it's not a very fun time for the security team at that company. And the main value of this is you don't want to have what's called the confused deputy problem where service A is talking to service B with their credential.

### Excerpt da transcript

Hello and welcome everyone. I'm here to talk to you today about workload identity for humans, a 12-factor approach. First, let me give you a little intro. My name is Vish Abrams. I'm the chief architect at Heroku and I'm excited to talk about workload identity. So, I think the best place to start is what the heck is workload identity? And I put down the simplest definition that I could come up with, which is that it's a unique identity assigned to a workload for secure resource access. So in the case of an app developer, that means your application is your workload and the secure resources you want to connect to are backend APIs, databases, caches, other applications and services that your application needs to access. What about for humans? This is where 12-factor comes in. How many of you are familiar with the 12factor manifesto? All right, it's been around for 12 13 years. Essentially, um you may have heard that actually we're recently open sourced it actually at the last CubeCon 6 months ago and we are working with the community to update it and bring in some new ideas.

So realistically the thing that made 12factor so powerful and has made it last so long is that at its root what it's doing is defining a contract or an interface between an application developer and a platform developer or an application and a platform. And what that means is that a developer who builds a 12-factor app can build an app that's portable across platform and a platform can run any 12actor app. So, I like to think of 12 factor as the place where those interface definitions live. Here's an example. Today, most application developers never have to worry about TLS termination for their app. All they do is they listen on a port and the platform magically directs traffic to their application. That allows them to build locally using localhost on whatever port they want. and then when they push their application into the cloud or onto an internal platform, it just runs and they don't have to worry about it. There are other examples that are not quite as standardized as this idea of port and TLS termination.

Here's one, domain names. So many times the application is agnostic to where it's running, but there are certain cases where it actually needs to know what domain it's being accessed on. A really great example is OOTH callbacks. If you're doing an OOTH integration, the callback you have to pass to the remote OOTH server includes your domain name so it can redirect back to you a
