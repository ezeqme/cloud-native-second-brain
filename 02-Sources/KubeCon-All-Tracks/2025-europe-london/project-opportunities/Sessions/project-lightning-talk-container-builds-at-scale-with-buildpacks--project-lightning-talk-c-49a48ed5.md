---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Project Opportunities"
themes: ["AI ML", "Runtime Containers", "SRE Reliability", "Community Governance"]
speakers: ["Joe Kutner", "Maintainer"]
sched_url: https://kccnceu2025.sched.com/event/1tcwd/project-lightning-talk-container-builds-at-scale-with-buildpacks-joe-kutner-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Container+Builds+at+Scale+with+Buildpacks+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: Container Builds at Scale with Buildpacks - Joe Kutner, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Runtime Containers]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Joe Kutner, Maintainer
- Schedule: https://kccnceu2025.sched.com/event/1tcwd/project-lightning-talk-container-builds-at-scale-with-buildpacks-joe-kutner-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Container+Builds+at+Scale+with+Buildpacks+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Container Builds at Scale with Buildpacks.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcwd/project-lightning-talk-container-builds-at-scale-with-buildpacks-joe-kutner-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Container+Builds+at+Scale+with+Buildpacks+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=8ULJg-z_wZA
- YouTube title: Project Lightning Talk: Container Builds At Scale With Buildpacks - Joe Kutner, Maintainer
- Match score: 0.933
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-container-builds-at-scale-with-buildpacks/8ULJg-z_wZA.txt
- Transcript chars: 7716
- Keywords: container, docker, images, application, caching, layers, salesforce, across, without, mechanisms, actually, rebuild, builders, builds, heroku, managing, terrence, called

### Resumo baseado na transcript

All right, we're going to talk about container builds at scale with build packs. Uh we're going to look at how companies like Salesforce, Google, Heroku, Bloomberg, and others are using cloudnative build packs to make managing container builds on their developer platforms more efficient. uh that in turn gives you composability because these build pack modules are designed to work together. And uh more importantly uh at CubeCon uh we have a maintainer track talk tomorrow uh at noon uh that Joe and one of the other uh contributors uh Joey will be doing if you want to learn more.

### Excerpt da transcript

All right, we're going to talk about container builds at scale with build packs. Uh we're going to look at how companies like Salesforce, Google, Heroku, Bloomberg, and others are using cloudnative build packs to make managing container builds on their developer platforms more efficient. Uh so build packs is an incubating CNCF project. Uh we've applied for graduation. Uh so we're starting that review process. Um you can learn more about that uh in our talk tomorrow which we'll give you some details on. Uh so when we talk about scale I want to be clear that I'm I'm talking about the order of tens of millions of images uh for some of these organizations. But the problems you encounter at that level of scale are for the most part the same as the problems that you have when you're managing thousands or even hundreds of images. Uh build packs work across this whole spectrum of scale. Uh, and they also stay with you as you grow. And we'll talk about how that works in a little bit. Uh, so real quick, my name is Joe Cutner.

I'm an architect working at Salesforce on our internal developer platform and I'm one of the co-founders of the BuildP packs project along with my other co-founder, Terrence. Hi, I'm Terrence. Uh, also co-founder on the build packs project. Uh, and I'm an architect at Salesforce. Cool. So, what are build packs? Well, at a very high level, there are tools that translate your application source code into a productionready container image without the need for a Docker file. Now, you can use Docker files with build packs. There's a thing called build packs build pack extensions that let them work together. Uh, but in reality, most people that use build packs aren't doing this. And that's because when you adopt build packs, you're really embracing this model of modularizing the logic that's required to build your applications so that you can then reuse it. Uh this is in contrast to docker file where uh the only equivalent is basically copying and pasting a docker file across dozens or more repos and then trying to keep them up to date.

Uh but with build packs you can put that logic into a module. You can use higher level programming languages to do that. And then you have an API that you can use to create layers intentionally. Again, in contrast to docker file where the layers are created sort of arbitrarily from statements in the docker file, uh build packs let you be intentional about what's going into each layer and also provide metadata about
