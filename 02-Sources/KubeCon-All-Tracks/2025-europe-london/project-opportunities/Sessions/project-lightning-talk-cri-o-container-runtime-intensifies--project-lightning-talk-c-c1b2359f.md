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
themes: ["AI ML", "Runtime Containers", "Community Governance"]
speakers: ["Sascha Grunert", "Maintainer"]
sched_url: https://kccnceu2025.sched.com/event/1tcue/project-lightning-talk-cri-o-container-runtime-intensifies-sascha-grunert-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+CRI-O%3A+Container+Runtime+Intensifies+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: CRI-O: Container Runtime Intensifies - Sascha Grunert, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Runtime Containers]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Sascha Grunert, Maintainer
- Schedule: https://kccnceu2025.sched.com/event/1tcue/project-lightning-talk-cri-o-container-runtime-intensifies-sascha-grunert-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+CRI-O%3A+Container+Runtime+Intensifies+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: CRI-O: Container Runtime Intensifies.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcue/project-lightning-talk-cri-o-container-runtime-intensifies-sascha-grunert-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+CRI-O%3A+Container+Runtime+Intensifies+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=ONuxsPWXNUU
- YouTube title: Project Lightning Talk: CRI-O: Container Runtime Intensifies - Sascha Grunert, Maintainer
- Match score: 0.897
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-cri-o-container-runtime-intensifies/ONuxsPWXNUU.txt
- Transcript chars: 4057
- Keywords: container, volume, artifact, artifacts, profile, forward, support, images, available, looking, actual, inspect, second, runtime, intensifies, everyone, cubecon, actually

### Resumo baseado na transcript

I'm Sasha, one of the maintainers of cryo and I really hope you all enjoy this beautiful cubecon the next days. It is actually a lightweight container and time built exactly for Kubernetes. So a ze profile is just a json block in a single file and cryctl will tell you that the image is now up to date but uh cryo will indicate that it's actually identified an artifact and put this artifact into the local storage by using their corresponding config media type and also like manifest mime type.

### Excerpt da transcript

So welcome everyone to container runtime intensifies. Uh we are speaking about cryo today. I'm Sasha, one of the maintainers of cryo and I really hope you all enjoy this beautiful cubecon the next days. So what is cryo? It is actually a lightweight container and time built exactly for Kubernetes. So means it's optimized for Kubernetes and we also like follow the Kubernetes release cycle. We implement the features directly for Kubernetes. But it's on the other side also OCI compatible. This means that we followed the open container initiative. So if something changes there, it will also change in cryo. It's part of the CNCF since 2019 and we graduated in 2023. So we are still in party mood uh with respect to that and we have more than 300 contributors all over the world which is like really nice and it's still growing. So we are looking forward to Cryo 133. So it will feature support for OCI artifacts and on the other side we also have direct support for the image volume beta queration which will come in Kubernetes 1.33 means we can then also like support something like web assembly NI plugins and we also have some experimental FreeBSD support and of course I would like to highlight all those bug fixes documentation improvements dependency updates deprecations and cleanups I think that's a huge shout out to everyone who maintains this project.

So, thank you for that. Um, we are really looking forward to the bright future of Cryo. Let's look at the OCI artifact support. Cryo is now able to pull artifacts into a dedicated storage side by side to actual container images. And this means that we can also list, inspect and also remove artifacts. Now, this is completely new. And we can also on top of that we can use artifacts as image volumes. So this enables like a huge amount of AI and ML use cases which we all look forward that you show us how you use the feature. Um but it also allows configuration distribution for like smaller artifacts and um like stacking the content of container images. So if you have a universal binary for example in a container image then you can reuse it in multiple images by just using an image volume. So let's just provide a small demo of that. You can now use kry cuddle to for example pull a zum profile which wasn't able which which weren't your able before. So a ze profile is just a json block in a single file and cryctl will tell you that the image is now up to date but uh cryo will indicate that it's actually identified an artifa
