---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Project Opportunities"
themes: ["AI ML", "Runtime Containers", "SRE Reliability"]
speakers: []
sched_url: https://kccnceu2024.sched.com/event/1aQXF/container-builds-at-scale-with-buildpacks-project-lightning-talk
youtube_search_url: https://www.youtube.com/results?search_query=Container+Builds+at+Scale+with+Buildpacks+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Container Builds at Scale with Buildpacks | Project Lightning Talk

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Runtime Containers]], [[SRE Reliability]]
- País/cidade: France / Paris
- Speakers: N/A
- Schedule: https://kccnceu2024.sched.com/event/1aQXF/container-builds-at-scale-with-buildpacks-project-lightning-talk
- Busca YouTube: https://www.youtube.com/results?search_query=Container+Builds+at+Scale+with+Buildpacks+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Container Builds at Scale with Buildpacks | Project Lightning Talk.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1aQXF/container-builds-at-scale-with-buildpacks-project-lightning-talk
- YouTube search: https://www.youtube.com/results?search_query=Container+Builds+at+Scale+with+Buildpacks+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=TX_UXuzqVGQ
- YouTube title: Container Builds at Scale with Buildpacks | Project Lightning Talk
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/container-builds-at-scale-with-buildpacks-project-lightning-talk/TX_UXuzqVGQ.txt
- Transcript chars: 5916
- Keywords: docker, images, container, layers, operating, without, running, buildpacks, talking, heroku, mechanism, builds, manage, google, millions, salesforce, themselves, actually

### Resumo baseado na transcript

okay we're going to talk about uh using Cloud native build packs to manage your container images at scale and when I say scale I'm talking about how companies like Google and Heroku and VMware manage tens of millions of images uh using build packs uh I'm Joe cutner and I just flew into Paris three hours ago so I am less awake than you are I'm one of the founders of the cloud buildpacks project and with me is Terence Lee uh I if I didn't say I I

### Excerpt da transcript

okay we're going to talk about uh using Cloud native build packs to manage your container images at scale and when I say scale I'm talking about how companies like Google and Heroku and VMware manage tens of millions of images uh using build packs uh I'm Joe cutner and I just flew into Paris three hours ago so I am less awake than you are I'm one of the founders of the cloud buildpacks project and with me is Terence Lee uh I if I didn't say I I work at UH Salesforce terance also works at Salesforce for Heroku so what are build packs build packs very simply are tools that transform your source code into container images without using a Docker file what you get is uh a Docker image that contains layers that map logically to your image components uh and it's well structured because the build packs are uh sharable right so once someone has written a build pack you can take advantage of all the things that they've put into it without having to handcraft or artisanally copy paste uh your Docker file to get just what you wanted so the build packs themselves are are actually modular units uh that encapsulate all the concerns associated with a particular technology uh like Java or go or Maven and then these build packs are composed together and executed by a build pack platform and we'll talk about how to run one of those in a second so you can use Docker file with build packs as an extension but it's not required and in fact most uh Bill pack users don't don't use Docker file at all so why use build packs well I can answer this uh by asking you a question how many of you have uh you know made a seemingly trivial change to your Docker file and then realize that uhoh you've busted every one of your cach layers and you have to rebuild from scratch and wait minutes or maybe longer cool now do that 10 million times it's not it's not really efficient right and that efficent at scale is really where build packs came from platforms that are managing that large of a you know a set of container images need a mechanism that that isn't so rigid the way that the docker file is so even if you're not managing tens of millions of images let's say you have 500 images 500 Java images or something like that you know everything's humming along fine you're building with Docker file you make commits and it rebuilds and then Along Comes A cve and every one of those images is now vulnerable and you have to patch it and update it well to do that with Docker file means especially if it's s
