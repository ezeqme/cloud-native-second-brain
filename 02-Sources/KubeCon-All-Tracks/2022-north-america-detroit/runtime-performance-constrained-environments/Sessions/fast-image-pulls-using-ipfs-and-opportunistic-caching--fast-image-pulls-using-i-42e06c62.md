---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2022 - Detroit, United States"
event_id: kccncna2022
year: 2022
region: "North America"
city: "Detroit"
country: "United States"
event_date: "2022-10-24/2022-10-28"
track: "Runtime Performance + Constrained Environments"
themes: ["AI ML", "Runtime Containers", "SRE Reliability"]
speakers: ["Christian Weichel", "Manuel de Brito Fontes", "Gitpod"]
sched_url: https://kccncna2022.sched.com/event/182JW/fast-image-pulls-using-ipfs-and-opportunistic-caching-christian-weichel-manuel-de-brito-fontes-gitpod
youtube_search_url: https://www.youtube.com/results?search_query=Fast+Image+Pulls+Using+IPFS+And+Opportunistic+Caching+CNCF+KubeCon+2022
slides: []
status: parsed
---

# Fast Image Pulls Using IPFS And Opportunistic Caching - Christian Weichel & Manuel de Brito Fontes, Gitpod

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Runtime Performance + Constrained Environments]]
- Temas: [[AI ML]], [[Runtime Containers]], [[SRE Reliability]]
- País/cidade: United States / Detroit
- Speakers: Christian Weichel, Manuel de Brito Fontes, Gitpod
- Schedule: https://kccncna2022.sched.com/event/182JW/fast-image-pulls-using-ipfs-and-opportunistic-caching-christian-weichel-manuel-de-brito-fontes-gitpod
- Busca YouTube: https://www.youtube.com/results?search_query=Fast+Image+Pulls+Using+IPFS+And+Opportunistic+Caching+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre Fast Image Pulls Using IPFS And Opportunistic Caching.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182JW/fast-image-pulls-using-ipfs-and-opportunistic-caching-christian-weichel-manuel-de-brito-fontes-gitpod
- YouTube search: https://www.youtube.com/results?search_query=Fast+Image+Pulls+Using+IPFS+And+Opportunistic+Caching+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=kS6aDScfVuw
- YouTube title: Fast Image Pulls Using IPFS And Opportunistic Caching - Christian Weichel & Manuel de Brito Fontes
- Match score: 0.801
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/fast-image-pulls-using-ipfs-and-opportunistic-caching/kS6aDScfVuw.txt
- Transcript chars: 27541
- Keywords: registry, images, content, facade, pulling, cluster, caching, essentially, question, within, upstream, workspace, manifest, actually, control, itself, layers, distribution

### Resumo baseado na transcript

thank you all for sticking around last day conference um appreciate you all showing up so we're going to talk about fast image polls using ipfs and opportunistic caching and my name is Chris I work at gitpod and with me on this stage should be Alejandro who is actually in a tab in a Google meet in this video browser right now so we'll pull them in later for the Q a session so we both work at gitpod and what we do is we turn the hours and

### Excerpt da transcript

thank you all for sticking around last day conference um appreciate you all showing up so we're going to talk about fast image polls using ipfs and opportunistic caching and my name is Chris I work at gitpod and with me on this stage should be Alejandro who is actually in a tab in a Google meet in this video browser right now so we'll pull them in later for the Q a session so we both work at gitpod and what we do is we turn the hours and days that it takes to set up a deaf environment into seconds and the reason I'm bringing that up is part of this deaf environment is a Docker image that you can choose or that we can build for you and so just to show a quick slightly sped up demo I was just on GitHub clicked the button and then it's preparing the workspace pulling the image right and this is the face this is exactly the thing that we're talking about initializing content and then you get ready to go def environment in this case vs code can be other IDs and the other I the fact that it can be other Ides will also become relevant later in the talk so that's what gitpod does and this is the context in which we're talking so we pull a lot of different images so over the any sort of period of seven days we'll pull more than ten thousand distinct images measured by their manifest not necessarily so they might have some layer overlap but it's um ten thousand distinct images and we cache more than a terabyte of um of image layers and these images vary greatly in size anywhere between 200 megabytes to several tens of gigabytes so it's and we have very little control over what images our users will bring so we have to be very Thrifty to make that fast so just to tell you a bit about where we're coming from from a Time perspective and where we've been heading so about 12 months ago when we embarked on a let's get this faster Journey P95 workspace startup times was more than 10 minutes and our Prometheus histogram just you know stopped at 10 minutes within like beyond that it doesn't matter um you're going to assume the system is broken anyways so more than 10 minutes and today we've brought this down to 120.

that is still a very long time to be waiting in front of a computer and until you come work so we'll keep on working bringing that down but this is by far the largest reduction that we've been able to achieve and a good part of this is because of the caching mechanisms that we'll discuss in this in this talk the p50 startup time more than halved as well so we're
