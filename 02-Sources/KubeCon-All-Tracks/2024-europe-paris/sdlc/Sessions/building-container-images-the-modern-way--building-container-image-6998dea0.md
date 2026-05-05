---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2024 - Paris, France"
event_id: kccnceu2024
year: 2024
region: "Europe"
city: "Paris"
country: "France"
event_date: "2024-03-19/2024-03-22"
track: "SDLC"
themes: ["AI ML", "Runtime Containers"]
speakers: ["Adrian Mouat", "Chainguard"]
sched_url: https://kccnceu2024.sched.com/event/1YeRB/building-container-images-the-modern-way-adrian-mouat-chainguard
youtube_search_url: https://www.youtube.com/results?search_query=Building+Container+Images+the+Modern+Way+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Building Container Images the Modern Way - Adrian Mouat, Chainguard

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[SDLC]]
- Temas: [[AI ML]], [[Runtime Containers]]
- País/cidade: France / Paris
- Speakers: Adrian Mouat, Chainguard
- Schedule: https://kccnceu2024.sched.com/event/1YeRB/building-container-images-the-modern-way-adrian-mouat-chainguard
- Busca YouTube: https://www.youtube.com/results?search_query=Building+Container+Images+the+Modern+Way+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Building Container Images the Modern Way.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1YeRB/building-container-images-the-modern-way-adrian-mouat-chainguard
- YouTube search: https://www.youtube.com/results?search_query=Building+Container+Images+the+Modern+Way+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=nZLz0o4duRs
- YouTube title: Building Container Images the Modern Way - Adrian Mouat, Chainguard
- Match score: 0.849
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/building-container-images-the-modern-way/nZLz0o4duRs.txt
- Transcript chars: 26360
- Keywords: images, docker, container, dagger, minimal, create, actually, everything, application, called, wolfie, reproducible, builds, static, interesting, saying, containers, probably

### Resumo baseado na transcript

it's gone quiet so I think that means I'm meant to start um so I really was not expecting to be in this room and I'm kind of astounded there so many people in this room are you sure you're in the right room you're laughing but um okay so my name is Adrian Mo um I'm a technical community advocate or Dev if you will for chain guard at chain guard we build minimal low cve container images so this is one of my favorite quotes about um containers build that's what you get so so um hang on can I a so in the what we're saying is appco build specified architecture then the build file which is build appco the name of the image which is going to be wolfy Bas so

### Excerpt da transcript

it's gone quiet so I think that means I'm meant to start um so I really was not expecting to be in this room and I'm kind of astounded there so many people in this room are you sure you're in the right room you're laughing but um okay so my name is Adrian Mo um I'm a technical community advocate or Dev if you will for chain guard at chain guard we build minimal low cve container images so this is one of my favorite quotes about um containers it's probably a decade old it's by Brian canell who is a you know if you ever get a chance to see a Brian canell talk do he's always amazing but he said Docker is doing to app what app did to toar so way back in the day we used to use tar balls to ship software around you know you just put your stuff in the tar.gz and send it around and that was okay it kind of worked but there was always problem s with dependencies we work in my machine but not on somebody else's machine um and then we start reducing things like putting stuff more stuff into the package managers and Linux distributions um and that was a lot better because our package managers would take care of figuring out the dependencies and so on and then Docker took it even a step further um by packaging everything up down to the operating system layer uh and that got us has much better reproducibility and solves this it works on my machine problem so that's kind of what that that quotes getting at but even if you look at your package manager formats your Debs your apks your RPMs Etc if you squint they're really just a tar ball plus a little bit of metadata around versions and dependencies there's not much else uh to and it's the same with container images they're really just packaging for an application it's just a file system and some metadata and theoretically at least they're not that difficult to create a container image there's even standards documents that tell you exactly what files you need to get in there to get a running oci container image so you might think well everybody will create their own container to but we've not really seen that happen or at least we've not really seen people create good container build tools we've may be seen a lot of build tools but not a lot of fantastic build [Music] tooling um so what are some of the things we would like to see in a image Builder well ideally if you want to your best of image Builder is going to be able to build min minimal image so what do I mean by that I mean like our image should only have our applic
