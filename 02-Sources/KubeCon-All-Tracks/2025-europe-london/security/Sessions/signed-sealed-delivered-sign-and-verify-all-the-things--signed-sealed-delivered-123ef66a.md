---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Security"
themes: ["Security"]
speakers: ["Jeremy Rickard", "Microsoft"]
sched_url: https://kccnceu2025.sched.com/event/1txCV/signed-sealed-delivered-sign-and-verify-all-the-things-jeremy-rickard-microsoft
youtube_search_url: https://www.youtube.com/results?search_query=Signed%2C+Sealed%2C+Delivered+-+Sign+and+Verify+All+the+Things+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Signed, Sealed, Delivered - Sign and Verify All the Things - Jeremy Rickard, Microsoft

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Security]]
- Temas: [[Security]]
- País/cidade: United Kingdom / London
- Speakers: Jeremy Rickard, Microsoft
- Schedule: https://kccnceu2025.sched.com/event/1txCV/signed-sealed-delivered-sign-and-verify-all-the-things-jeremy-rickard-microsoft
- Busca YouTube: https://www.youtube.com/results?search_query=Signed%2C+Sealed%2C+Delivered+-+Sign+and+Verify+All+the+Things+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Signed, Sealed, Delivered - Sign and Verify All the Things.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txCV/signed-sealed-delivered-sign-and-verify-all-the-things-jeremy-rickard-microsoft
- YouTube search: https://www.youtube.com/results?search_query=Signed%2C+Sealed%2C+Delivered+-+Sign+and+Verify+All+the+Things+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=g--50XLcqRw
- YouTube title: Signed, Sealed, Delivered - Sign and Verify All the Things - Jeremy Rickard, Microsoft
- Match score: 0.892
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/signed-sealed-delivered-sign-and-verify-all-the-things/g--50XLcqRw.txt
- Transcript chars: 29278
- Keywords: registry, flux, images, running, notation, verify, github, voting, container, everything, signature, signed, cluster, pretty, action, install, application, called

### Resumo baseado na transcript

All right, thank you so much for making the trek all the way back over here again. Um thanks for coming to sign sealed and delivered sign and verify all the things. It made demos at CubeCon or other conferences really, really easy as long as the Wi-Fi was working and just kind of gave you this kind of carefree experience. We're going to talk about supply chain security and how it applies to deploying an application. I ran into this running getting ready for this application or for this demo because these images uh are originally are in DockerHub. But in production, you may end up getting hit with a rate limit when you're trying to do a scale operation or spin up a new application and that's just kind of painful.

### Excerpt da transcript

All right, thank you so much for making the trek all the way back over here again. I'm sure everybody was here this morning. Uh it's good to see everybody back in here. Um thanks for coming to sign sealed and delivered sign and verify all the things. My name is Jeremy Rickard. I am a principal software engineer at Microsoft Azure. Um and also a co-chair of SIG release in the Kubernetes project. Today we're going to talk um a little bit about container supply chain security with a large focus on um signing images and doing verification for that and how we can use that to verify the authenticity of our resources. Some of what we're going to cover today uh are things that I've picked up uh in my day job. In my day job, I help build and publish a lot of CNCF projects for use inside of Azure and Microsoft as a whole. Also things from SIG release and other things I've I've seen and learned about in other projects. But let's start off uh taking a minute to reminisce about the early days, maybe the easier days of computing uh with containers.

For me, I found containers probably around 2017ish. Uh and I was kind of drawn to it because I found that it was really easy for me to package up my application and get it to run in a really similar way to how it did on my my desktop. You were basically a Docker push away from getting something up and running. and and a lot of things were free in that time, you know, in 2017. I could push something to DockerHub and then I could deploy it to production and it was just kind of free and it worked and it was really cool. It made demos at CubeCon or other conferences really, really easy as long as the Wi-Fi was working and just kind of gave you this kind of carefree experience. So, with that in mind and reminiscing, I thought that I would try to deploy an application as part of this talk. We're going to talk about supply chain security and how it applies to deploying an application. So, I thought I would find something kind of old. Um, here we have the emoji vote app. It's uh I think it was published by Buoyant in 2017.

So, we're we're coming up on a long time on this thing. And yesterday there was an election in my my home of Colorado. Uh that was almost entirely pointless. So, having this as a voting app seems like a really good idea. Uh I found this thing on the internet. Uh it's from 2017. It's probably going to be completely fine and and all right, right? We're going to we're going to deploy it. There will be no issues what
