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
speakers: ["Krisztian Litkey", "Intel", "Mike Brown", "IBM"]
sched_url: https://kccncna2022.sched.com/event/182JT/nri-extending-containerd-and-cri-o-with-common-plugins-krisztian-litkey-intel-mike-brown-ibm
youtube_search_url: https://www.youtube.com/results?search_query=NRI%3A+Extending+Containerd+And+CRI-O+With+Common+Plugins+CNCF+KubeCon+2022
slides: []
status: parsed
---

# NRI: Extending Containerd And CRI-O With Common Plugins - Krisztian Litkey, Intel & Mike Brown, IBM

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2022 - Detroit, United States
- Trilha oficial: [[Runtime Performance + Constrained Environments]]
- Temas: [[AI ML]], [[Runtime Containers]], [[SRE Reliability]]
- País/cidade: United States / Detroit
- Speakers: Krisztian Litkey, Intel, Mike Brown, IBM
- Schedule: https://kccncna2022.sched.com/event/182JT/nri-extending-containerd-and-cri-o-with-common-plugins-krisztian-litkey-intel-mike-brown-ibm
- Busca YouTube: https://www.youtube.com/results?search_query=NRI%3A+Extending+Containerd+And+CRI-O+With+Common+Plugins+CNCF+KubeCon+2022

## Resumo

Sessão da KubeCon sobre NRI: Extending Containerd And CRI-O With Common Plugins.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2022.sched.com/event/182JT/nri-extending-containerd-and-cri-o-with-common-plugins-krisztian-litkey-intel-mike-brown-ibm
- YouTube search: https://www.youtube.com/results?search_query=NRI%3A+Extending+Containerd+And+CRI-O+With+Common+Plugins+CNCF+KubeCon+2022
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=BOaW99BFbdA
- YouTube title: NRI: Extending Containerd And CRI-O With Common Plugins - Krisztian Litkey, Intel & Mike Brown, IBM
- Match score: 0.82
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2022/nri-extending-containerd-and-cri-o-with-common-plugins/BOaW99BFbdA.txt
- Transcript chars: 33657
- Keywords: container, runtime, plugins, plugin, containers, events, resource, basically, configuration, customizations, little, actually, request, implement, creation, update, runtimes, specification

### Resumo baseado na transcript

thanks for coming to our pitch um we're going to talk about node resources it's a node resource well you've probably heard of kubernetes and kublet and container run times maybe and anybody needs to know a little bit more about container runtime raise your hand if you're good if you're if you understand what those are that then that's great hey about I'd say about six years ago I'm just gonna do a little intro a little history before handing off to Christian about six years ago we were

### Excerpt da transcript

thanks for coming to our pitch um we're going to talk about node resources it's a node resource well you've probably heard of kubernetes and kublet and container run times maybe and anybody needs to know a little bit more about container runtime raise your hand if you're good if you're if you understand what those are that then that's great hey about I'd say about six years ago I'm just gonna do a little intro a little history before handing off to Christian about six years ago we were sitting around a round table doing the open container specification for runtime specifications and a guy named Bernal Patel I don't know if he's here or not but Ronald Patel came up with an idea to do hooks in inside of the Run C runtime using some text that would go into the oci specification and those hooks would be executable programs that will be run at particular points at which a container is executed for example pre-start post start you know that kind of thing but how would people Define were that where would they put them okay uh there would just be a path in the oci spec to where these hook these application programs would be that would actually receive the contents of the oci spec maybe some State and then reply back um you know synchronously in with maybe some modifications to the oci spec or they would do an attach or a resource and that's where no resource comes in the reason that people need to extend the these container runtime engines if you will underneath the covers is because resource managers need to be able to modify how the containers get access to the resources how much resources they get and we we try to do some configuration if you will in the container runtimes but we always seem to get it wrong and resource managers need to not just manage the resource for pods and containers but also they need to manage the resources for Docker containers for you know other kinds of container runtimes that are running in parallel on your node paired in parallel with kubelet and worker node pods that have been assigned and Intel is one of the the groups that always needed to be able to have their own resource managers and so they're heavily involved we we did do Beyond this whole thing we didn't know ceiling spec we contained runtime groups put together this runtime schema for for our hook schema sorry that would sit on a directory and then a container runtime could bring in that schema or look at look at the Json for anybody who wants to do a resource book inside
