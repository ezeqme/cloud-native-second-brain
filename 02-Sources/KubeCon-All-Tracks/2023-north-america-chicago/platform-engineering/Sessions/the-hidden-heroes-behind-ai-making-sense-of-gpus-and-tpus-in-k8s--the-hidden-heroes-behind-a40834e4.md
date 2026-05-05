---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2023 - Chicago, United States"
event_id: kccncna2023
year: 2023
region: "North America"
city: "Chicago"
country: "United States"
event_date: "2023-11-06/2023-11-09"
track: "Platform Engineering"
themes: ["AI ML", "Platform Engineering"]
speakers: ["David Porter", "Google", "Evan Lezar", "NVIDIA"]
sched_url: https://kccncna2023.sched.com/event/1R2sf/the-hidden-heroes-behind-ai-making-sense-of-gpus-and-tpus-in-k8s-david-porter-google-evan-lezar-nvidia
youtube_search_url: https://www.youtube.com/results?search_query=The+Hidden+Heroes+Behind+AI%3A+Making+Sense+of+GPUs+and+TPUs+in+K8s+CNCF+KubeCon+2023
slides: []
status: parsed
---

# The Hidden Heroes Behind AI: Making Sense of GPUs and TPUs in K8s - David Porter, Google & Evan Lezar, NVIDIA

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2023 - Chicago, United States
- Trilha oficial: [[Platform Engineering]]
- Temas: [[AI ML]], [[Platform Engineering]]
- País/cidade: United States / Chicago
- Speakers: David Porter, Google, Evan Lezar, NVIDIA
- Schedule: https://kccncna2023.sched.com/event/1R2sf/the-hidden-heroes-behind-ai-making-sense-of-gpus-and-tpus-in-k8s-david-porter-google-evan-lezar-nvidia
- Busca YouTube: https://www.youtube.com/results?search_query=The+Hidden+Heroes+Behind+AI%3A+Making+Sense+of+GPUs+and+TPUs+in+K8s+CNCF+KubeCon+2023

## Resumo

Sessão da KubeCon sobre The Hidden Heroes Behind AI: Making Sense of GPUs and TPUs in K8s.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2023.sched.com/event/1R2sf/the-hidden-heroes-behind-ai-making-sense-of-gpus-and-tpus-in-k8s-david-porter-google-evan-lezar-nvidia
- YouTube search: https://www.youtube.com/results?search_query=The+Hidden+Heroes+Behind+AI%3A+Making+Sense+of+GPUs+and+TPUs+in+K8s+CNCF+KubeCon+2023
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=H5gN8fHn3fo
- YouTube title: The Hidden Heroes Behind AI: Making Sense of GPUs and TPUs in K8s - David Porter & Evan Lezar
- Match score: 0.922
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2023/the-hidden-heroes-behind-ai-making-sense-of-gpus-and-tpus-in-k8s/H5gN8fHn3fo.txt
- Transcript chars: 45304
- Keywords: device, devices, actually, plugin, container, gpu, workload, access, plug-in, inference, resource, specific, request, basically, workloads, information, vendor, server

### Resumo baseado na transcript

all right I think it's time to start thanks for the jokes um so welcome to our session thank you for sticking around till the last session of the day also walking to the you know last part of the building uh Welcome to our session the hidden Heroes behind AI making sense of gpus and tpus and kubernetes uh my name is David Porter U from Google I work on the Google kubernetes team I work on node I'm also a maintainer and in Sig node and this is

### Excerpt da transcript

all right I think it's time to start thanks for the jokes um so welcome to our session thank you for sticking around till the last session of the day also walking to the you know last part of the building uh Welcome to our session the hidden Heroes behind AI making sense of gpus and tpus and kubernetes uh my name is David Porter U from Google I work on the Google kubernetes team I work on node I'm also a maintainer and in Sig node and this is Evan hi I'm Yan uh I am with Nvidia as the tarch says uh I'm on the cloud native team and we build everything that's required to run gpus in containers right so the container toolkit if you've heard of that the device plugin uh the GPU operator all of that good stuff um so like these kinds of devices and accelerators have been quite a Hot Topic at this conference already and they're becoming increasingly important to run these complex workloads like uh machine learning training and inference and the demand for them has been growing over time as well so it's even more important for us to keep be able to access these gpus tpus and even the fpgas uh in our kubernetes um clusters so that we can run these jobs so in the talk today we'll cover how kubernetes actually integrates with these devices and sort of a little bit of a spoiler but it's through device plugins and how these device plugins and device allocation actually work uh we also be looking like some usage examples of gpus and tpus on kubernetes and giving some sort of thoughts details hints tips on operating clusters with TPU tpus and gpus and a sort of a brief outlook on what we see as the future of devices in kubernetes now first of all what is a device well essentially it's this thing here right but that's not very useful um so a device with a capital d uh or resource is something that a user wants access to for a specific purpose such as training a machine learning model um and but one you sort of like go down the various levels of abstraction or up through the various levels of abstraction I suppose uh you end up with a collection of device nodes libraries and utilities that are required to actually access to this device in in an environment such as a container and in kubernetes these are exposed as countable extended resources which can then be requested by a user and in order to do this one requires a per node device plugin so these device plugins register with a cubet and sort of under a specific name such as nvidia.com GPU which I'm sure some of you have
