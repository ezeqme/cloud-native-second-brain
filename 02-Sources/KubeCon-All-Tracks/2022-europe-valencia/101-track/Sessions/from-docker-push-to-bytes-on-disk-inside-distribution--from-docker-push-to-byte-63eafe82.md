---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain"
event_id: kccnceu2022
year: 2022
region: "Europe"
city: "Valencia"
country: "Spain"
event_date: "2022-05-16/2022-05-20"
track: "101 Track"
themes: ["101 Track"]
speakers: ["Wayne Warren", "Adam Wolfe Gordon", "DigitalOcean"]
sched_url: https://kccnceu2022.sched.com/event/ytqU/from-docker-push-to-bytes-on-disk-inside-distribution-wayne-warren-adam-wolfe-gordon-digitalocean
youtube_search_url: https://www.youtube.com/results?search_query=From+%60docker+push%60+to+Bytes+on+Disk%3A+Inside+Distribution+CNCF+KubeCon+2022
slides: []
status: parsed
---

# From `docker push` to Bytes on Disk: Inside Distribution - Wayne Warren & Adam Wolfe Gordon, DigitalOcean

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2022 - Valencia, Spain
- Trilha oficial: [[101 Track]]
- Temas: [[101 Track]]
- País/cidade: Spain / Valencia
- Speakers: Wayne Warren, Adam Wolfe Gordon, DigitalOcean
- Schedule: https://kccnceu2022.sched.com/event/ytqU/from-docker-push-to-bytes-on-disk-inside-distribution-wayne-warren-adam-wolfe-gordon-digitalocean
- Busca YouTube: https://www.youtube.com/results?search_query=From+%60docker+push%60+to+Bytes+on+Disk%3A+Inside+Distribution+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre From `docker push` to Bytes on Disk: Inside Distribution.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2022.sched.com/event/ytqU/from-docker-push-to-bytes-on-disk-inside-distribution-wayne-warren-adam-wolfe-gordon-digitalocean
- YouTube search: https://www.youtube.com/results?search_query=From+%60docker+push%60+to+Bytes+on+Disk%3A+Inside+Distribution+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=XQatzE7tZDE
- YouTube title: From `docker push` to Bytes on Disk: Inside Distribution - Wayne Warren & Adam Wolfe Gordon
- Match score: 0.854
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/from-docker-push-to-bytes-on-disk-inside-distribution/XQatzE7tZDE.txt
- Transcript chars: 32684
- Keywords: registry, upload, container, distribution, digest, manifest, request, layers, client, garbage, docker, collection, session, storage, images, question, pushing, little

### Resumo baseado na transcript

all right i think we're good to go good afternoon uh welcome to from docker push to bites on disc my name is wayne warren and i'm a senior engineer at digital ocean i work on the digital ocean kubernetes product and the digital ocean container registry product i'm adam wolf gordon i work with wayne and digilotion or i'm also a senior engineer today we're going to talk about container registries and we're going to talk about what they are and how they work and give a bunch of a customer who has a problem with a container registry um but yeah if so so that's the only one that distribution calculates by default if at the end of a chunked upload uh the digest really shocked 512 then distribution will go and download

### Excerpt da transcript

all right i think we're good to go good afternoon uh welcome to from docker push to bites on disc my name is wayne warren and i'm a senior engineer at digital ocean i work on the digital ocean kubernetes product and the digital ocean container registry product i'm adam wolf gordon i work with wayne and digilotion or i'm also a senior engineer today we're going to talk about container registries and we're going to talk about what they are and how they work and give a bunch of those details before we get into the details though i did want to give a little bit of a disclaimer which is that container registries can do a lot of stuff these days they can store artifacts and things that aren't containers they can have additional metadata like bills and materials and signatures and things like that and we are going to ignore all of that today this talk is in the 101 track so we're going to stick to the most basic use case of pushing and pulling container images from your registry before we get into a bunch of details let's answer a really basic question what is a container registry to answer that let's start with something most of us have probably seen or done before and that's a docker push so you docker push some ascii arrows fly across the screen and your container image is now somewhere in the cloud later your co-worker or some random stranger in the internet or a deployment system can pull that image and run it somewhere else so this is the power of containers as we all know you can share the image and it should just run on somebody else's computer the thing that stores those images in the cloud that's a container registry so we know what a container registry does for us but what's underneath it's a content addressable data store and what does that mean it's an object store so it you can put data there and it's content addressable that means that for each object in that store instead of being identified by some arbitrary key or path name it's identified by a digest of its contents in container in a container registry we have a few different kinds of objects first we have blobs these are the the basic object that uh that are stored in a container registry and then we have manifests they are which are metadata about images and the contents of the blobs so they tell us what layer blobs are stored in each image you can think of manifest as a set of pointers to layers and then finally we have tags so tags here are drawn as a different shape because they're special
