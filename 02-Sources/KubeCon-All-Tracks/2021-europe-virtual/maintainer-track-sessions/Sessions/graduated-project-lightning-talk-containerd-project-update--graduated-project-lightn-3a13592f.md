---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual"
event_id: kccnceu2021
year: 2021
region: "Europe"
city: "Virtual"
country: "Virtual"
event_date: "2021-05-04/2021-05-07"
track: "Maintainer Track Sessions"
themes: ["AI ML", "Runtime Containers", "Community Governance"]
speakers: ["Derek McGowan"]
sched_url: https://kccnceu2021.sched.com/event/iaAm/graduated-project-lightning-talk-containerd-project-update-derek-mcgowan
youtube_search_url: https://www.youtube.com/results?search_query=Graduated+Project+Lightning+Talk%3A+containerd+Project+Update+CNCF+KubeCon+2021
slides: []
status: parsed
---

# Graduated Project Lightning Talk: containerd Project Update - Derek McGowan

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2021 - Virtual, Virtual
- Trilha oficial: [[Maintainer Track Sessions]]
- Temas: [[AI ML]], [[Runtime Containers]], [[Community Governance]]
- País/cidade: Virtual / Virtual
- Speakers: Derek McGowan
- Schedule: https://kccnceu2021.sched.com/event/iaAm/graduated-project-lightning-talk-containerd-project-update-derek-mcgowan
- Busca YouTube: https://www.youtube.com/results?search_query=Graduated+Project+Lightning+Talk%3A+containerd+Project+Update+CNCF+KubeCon+2021

## Resumo

Sessão da KubeCon sobre Graduated Project Lightning Talk: containerd Project Update.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2021.sched.com/event/iaAm/graduated-project-lightning-talk-containerd-project-update-derek-mcgowan
- YouTube search: https://www.youtube.com/results?search_query=Graduated+Project+Lightning+Talk%3A+containerd+Project+Update+CNCF+KubeCon+2021
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=oEfNQfo1DpU
- YouTube title: Graduated Project Lightning Talk: containerd Project Update - Derek McGowan
- Match score: 0.972
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2021/graduated-project-lightning-talk-containerd-project-update/oEfNQfo1DpU.txt
- Transcript chars: 7018
- Keywords: container, images, running, cuddle, alpine, continuity, projects, client, library, allows, docker, output, created, quickly, called, components, runtimes, snapshotter

### Resumo baseado na transcript

hello welcome to the container d sub project lightning talk today we're going to give a brief overview of containerd's subprojects we will quickly go over the different projects and what it takes to become a container d sub project we will also have a demo of kennedy's latest subproject called nerd ctl or nerd cuddle if you prefer first though let's briefly go over what continuity is and what its architecture looks like container d is a container runtime designed to be simple stable and easily customized using plugins

### Excerpt da transcript

hello welcome to the container d sub project lightning talk today we're going to give a brief overview of containerd's subprojects we will quickly go over the different projects and what it takes to become a container d sub project we will also have a demo of kennedy's latest subproject called nerd ctl or nerd cuddle if you prefer first though let's briefly go over what continuity is and what its architecture looks like container d is a container runtime designed to be simple stable and easily customized using plugins think of it more as a resource manager for everything related to containers whether that is container file systems or the container execution environment continuity keeps track of it architecturally continuity is divided into simple components and accessed via grpc apis it communicates with lower level container runtimes which do the actual container execution via grpc like protocol called ttrpc different components of container d can also have plugins as well such as custom snapshotters or content stores continuity also has a fat client model meaning clients can import the go library and use different interface implementations the client can directly use containerities components to implement whatever it needs which allows it to do things like building or distributing images any way at once this leads to the first sub-project image crypt this tool in library makes use of continuity's extension points to support encrypted containers it contains a command to encrypt and decrypt images from a client it also has a stream processor which allows container to e to decrypt images during the unpack phase of a poll this can be enabled by configuring a stream processor plugin in container d which is configured to handle specific media types and images in this case the media type is an encrypted tar archive next let's take a look at the star gz snapshotter this snapshotter enables lazy pulling of any image which has layers in the star gz format the sarg format is a backwards compatible form of a gzip tar but with an extra index that allows retrieving individual files the star gc snapshotter utilizes this design to quickly start a container before all the file system content is locally available you can see by the benchmarks that this has a huge impact on container startup time this is also advantageous since in many cases the container processes never even read a majority of the container's file system this can be enabled in container d as a proxy plugi
