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
themes: ["AI ML", "Networking", "Community Governance"]
speakers: ["Liz Rice", "Christine Kim", "Isovalent", "Nico Meisenzahl", "white duck", "Vlad Ungureanu", "Palantir Technologies"]
sched_url: https://kccnceu2024.sched.com/event/1Yhfl/cilium-connecting-observing-and-securing-service-mesh-and-beyond-with-ebpf-liz-rice-christine-kim-isovalent-nico-meisenzahl-white-duck-vlad-ungureanu-palantir-technologies
youtube_search_url: https://www.youtube.com/results?search_query=Cilium%3A+Connecting%2C+Observing%2C+and+Securing+Service+Mesh+and+Beyond+with+eBPF+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Cilium: Connecting, Observing, and Securing Service Mesh and Beyond with eBPF - Liz Rice & Christine Kim, Isovalent; Nico Meisenzahl, white duck; Vlad Ungureanu, Palantir Technologies

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2024 - Paris, France
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Networking]], [[Community Governance]]
- País/cidade: France / Paris
- Speakers: Liz Rice, Christine Kim, Isovalent, Nico Meisenzahl, white duck, Vlad Ungureanu, Palantir Technologies
- Schedule: https://kccnceu2024.sched.com/event/1Yhfl/cilium-connecting-observing-and-securing-service-mesh-and-beyond-with-ebpf-liz-rice-christine-kim-isovalent-nico-meisenzahl-white-duck-vlad-ungureanu-palantir-technologies
- Busca YouTube: https://www.youtube.com/results?search_query=Cilium%3A+Connecting%2C+Observing%2C+and+Securing+Service+Mesh+and+Beyond+with+eBPF+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Cilium: Connecting, Observing, and Securing Service Mesh and Beyond with eBPF.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2024.sched.com/event/1Yhfl/cilium-connecting-observing-and-securing-service-mesh-and-beyond-with-ebpf-liz-rice-christine-kim-isovalent-nico-meisenzahl-white-duck-vlad-ungureanu-palantir-technologies
- YouTube search: https://www.youtube.com/results?search_query=Cilium%3A+Connecting%2C+Observing%2C+and+Securing+Service+Mesh+and+Beyond+with+eBPF+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=wq1TxZw1AaY
- YouTube title: Cilium: Connecting, Observing, and Securing Service Mesh and Beyond with eBPF - Panel
- Match score: 1.041
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/cilium-connecting-observing-and-securing-service-mesh-and-beyond-with/wq1TxZw1AaY.txt
- Transcript chars: 23758
- Keywords: cluster, celium, basically, clusters, security, started, network, authentication, inside, mutual, observability, decided, tetragon, running, traffic, container, policies, runtime

### Resumo baseado na transcript

should we get started yeah let's do it all right thank you everyone for being here this afternoon if you have got a seat next to you raise your hand I know there are some people outside I think you've done an awesome job of packing yourselves in beautifully uh thank you for being here thank you everyone who's tried to come in hopefully you're going to watch on YouTube later and catch up with all the latest updates from the San project can we start with a quick show you found it what benefits you've had maybe what problems you encountered along the way as well uh so we want to hear those studies and uh we would be delighted to publish those on the website so I think that is all the updates

### Excerpt da transcript

should we get started yeah let's do it all right thank you everyone for being here this afternoon if you have got a seat next to you raise your hand I know there are some people outside I think you've done an awesome job of packing yourselves in beautifully uh thank you for being here thank you everyone who's tried to come in hopefully you're going to watch on YouTube later and catch up with all the latest updates from the San project can we start with a quick show of hands how many of you H are already using say celium pretty good number of you okay awesome do we have any people here who have contributed to yeah smaller number but we very much appreciate your work okay fantastic so yeah welcome to cyan my name is Liz rice I work for is surveillant which is the company that originally created the celum project which consists of several pieces the three main parts are cium itself the networking component that you probably all know and love uh which provides networking capabilities incredibly high performance incredibly scalable and has kind of become the defacto networking solution in the cloud native World complimenting that there's Hubble which provides Network observability that you can use alongside celium and then finally there is the the new cousin in the selum family which is tetragon can we get a show of hands anyone here using tetragon yeah quite a few of you good so run runtime security and observability all of these things based on the amazing technology that is ebpf and uh as you probably all know I'm a massive fan of ebpf have a quick look at tetragon um since it's newer and maybe less familiar to uh some of the in the audience tetragon reached 1.0 status just in time for the last cucon in North America so it's providing runtime security and observability by hooking into all kinds of really interesting events in the kernel things like file access network access privilege escalation all the things that the colonel is responsible for we can hook into the into the kernel using ubf and provide these incredible uh detailed information about what may be security relevant events what's more we can filter those events in the kernel and that means it's incredibly uh high performance very very low overhead we've seen some measurements doing some very kind of useful um observability running at less than 2% CPU overhead which is well worthwhile to catch things like access to sensitive files that you're not expecting okay so we have just re released a few w
