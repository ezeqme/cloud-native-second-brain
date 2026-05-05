---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "Maintainer Track"
themes: ["AI ML", "Runtime Containers", "SRE Reliability", "Community Governance"]
speakers: ["Juan Bustamante", "Broadcom", "Aidan Delaney", "Bloomberg"]
sched_url: https://kccnceu2024.sched.com/event/1Yhj6/container-image-workflows-at-scale-with-buildpacks-juan-bustamante-broadcom-aidan-delaney-bloomberg
youtube_search_url: https://www.youtube.com/results?search_query=Container+Image+Workflows+at+Scale+with+Buildpacks+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Container Image Workflows at Scale with Buildpacks - Juan Bustamante, Broadcom & Aidan Delaney, Bloomberg

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Runtime Containers]], [[SRE Reliability]], [[Community Governance]]
- País/cidade: France / Paris
- Speakers: Juan Bustamante, Broadcom, Aidan Delaney, Bloomberg
- Schedule: https://kccnceu2024.sched.com/event/1Yhj6/container-image-workflows-at-scale-with-buildpacks-juan-bustamante-broadcom-aidan-delaney-bloomberg
- Busca YouTube: https://www.youtube.com/results?search_query=Container+Image+Workflows+at+Scale+with+Buildpacks+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Container Image Workflows at Scale with Buildpacks.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1Yhj6/container-image-workflows-at-scale-with-buildpacks-juan-bustamante-broadcom-aidan-delaney-bloomberg
- YouTube search: https://www.youtube.com/results?search_query=Container+Image+Workflows+at+Scale+with+Buildpacks+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=cenTw6WzQv8
- YouTube title: Container Image Workflows at Scale with Buildpacks - Juan Bustamante & Aidan Delaney
- Match score: 0.849
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/container-image-workflows-at-scale-with-buildpacks/cenTw6WzQv8.txt
- Transcript chars: 28751
- Keywords: images, builder, application, source, command, create, package, repository, probably, native, production, output, support, answer, manifest, buildpacks, existing, google

### Resumo baseado na transcript

it's like writing for the referee at the start of a a rugby game where they're looking to the sidelines saying when's the camera starting Miss referee oh okay um welcome to Paris um at half five in the evening and we have a full house I'm really impressed well done with your staying power folks this is this is really cool um as you probably know because you read the title of the talk uh Juan and I are here to represent the cloud natives bills pack Cloud native the usual manner now on this slide I'm using podman to Launch the backend service on Port 8880 but you could use Docker or you could use uh kubernetes or if you're really cool you could just directly invoke runy so this run is my for SL dos does demonstrate how to integrate pack with tecton as well but if I've not mentioned your favorite CI system then please do look at at our documentation for a longer list of Integrations and we're open to PRS if you've got an and we get the bite forbite reproducibility so kind of in summary we've looked at uh how to build images using the pack CLI we've had a little look at how to build images using the kpac kubernetes operator and we've had a look at various Network and information security directives and particularly under the sector specific obligations such as the digital operations resilience act I'm a technologist I need more uh operational things then the legislation and...

### Excerpt da transcript

it's like writing for the referee at the start of a a rugby game where they're looking to the sidelines saying when's the camera starting Miss referee oh okay um welcome to Paris um at half five in the evening and we have a full house I'm really impressed well done with your staying power folks this is this is really cool um as you probably know because you read the title of the talk uh Juan and I are here to represent the cloud natives bills pack Cloud native pill packs project um I suppose the first thing to do say upfront is that I'm going to do a little introduction for the first 10 minutes or so this is a maintainer track talk so some folks are going to expect some more technical details which Juan is going to go into and then we'll uh we'll conclude at the end with um some some stuff that everybody might be interested in as well so clar native Bill packs what we do with clar Native Bill packs is that we we we develop a specification hosted at bills. now there are multiple implementations of this specification all of them though share the same intention what we want to do is transform source project into production application images uh Bill packs do this by understanding your existing applications build system so for example understanding npm if you are building a node.js application and we essentially orchestrate the build using your existing build system but output an oci image a Docker image that you can then use to deploy on kubernetes so we want to start with some kind of application Source I've got a demo here which I'm not going to show you the source but trust me I'm a professional it has a a go backend or a back end written in go and it's got a front end written in typescript which needs to be compiled down into JavaScript and then served up using engine X or something and what we're going to do to build this is we're going to install the pack CLI from Bill packs.

that's our command line tool called pack and then I'm going to choose a builder image you can see the command at the top of the screen I'm going to choose a builder image and a builder image is a set of build packs a collection of build packs we just packaged them all into a single oci image for distribution and here I'm going to use a set of build packs from The Marvelous petto project an open source project however I could have chosen build packs from Heroku who make an excellent set of Bill packs or I could have chosen a set of Bill packs from Google because they specialize the
