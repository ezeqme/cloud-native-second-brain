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
themes: ["AI ML", "Security", "Platform Engineering", "Community Governance"]
speakers: ["Andrew Block", "Maintainer"]
sched_url: https://kccnceu2025.sched.com/event/1tcun/project-lightning-talk-oras-create-and-distribute-a-multi-platform-image-with-security-posture-andrew-block-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+ORAS%3A+Create+and+Distribute+a+Multi-platform+Image+with+Security+Posture+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Project Lightning Talk: ORAS: Create and Distribute a Multi-platform Image with Security Posture - Andrew Block, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Security]], [[Platform Engineering]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Andrew Block, Maintainer
- Schedule: https://kccnceu2025.sched.com/event/1tcun/project-lightning-talk-oras-create-and-distribute-a-multi-platform-image-with-security-posture-andrew-block-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+ORAS%3A+Create+and+Distribute+a+Multi-platform+Image+with+Security+Posture+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: ORAS: Create and Distribute a Multi-platform Image with Security Posture.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcun/project-lightning-talk-oras-create-and-distribute-a-multi-platform-image-with-security-posture-andrew-block-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+ORAS%3A+Create+and+Distribute+a+Multi-platform+Image+with+Security+Posture+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=2zjxSKAkT9E
- YouTube title: Project Lightning Talk: ORAS: Create and Distribute a Multi-platform Image with Secu... Andrew Block
- Match score: 0.979
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/project-lightning-talk-oras-create-and-distribute-a-multi-platform-ima/2zjxSKAkT9E.txt
- Transcript chars: 5028
- Keywords: artifacts, images, inside, allows, artifact, actually, create, registries, everything, compatible, manifest, distribute, multiarchchitect, registry, multiplatform, format, environments, available

### Resumo baseado na transcript

I'm a distinguished architect at Red Hat and a maintainer on the auras project. Just going to talk to you for a few moments just to speak about how we handle multiarchchitect images and distributed them using auras. A multiplatform image means that you can distribute a single image or artifact and have it be compatible with multiple architectures. You can add annotations, other metadata that you can then then query and then be able to process against it. Let's just do a quick demo of how we would go ahead and use auras to util actually build uh a multiplatform artifact. A manifest list allows us to then allow us to declare multiple architectures in inside a single reference.

### Excerpt da transcript

Hey everyone, my name is Andrew Black. I'm a distinguished architect at Red Hat and a maintainer on the auras project. Just going to talk to you for a few moments just to speak about how we handle multiarchchitect images and distributed them using auras. Now, how many of you show of hands have used auras or know of auras? Well, basically it is a CLI and set of binaries for managing OCI artifacts. OCI artifacts is a space that I have been very interested in for the last several years, especially when it comes to a lot of the new cloudnative patterns that have been coming up to speed in the last few years. It is really starting to take hold of why we're able to leverage a lot of the same technologies that we've used over the course of the last decade in cloud native for new ways of managing assets in container registries. Now, how many of you didn't know you could actually store items other than container images inside registries? The best part about that means that you can take advantage of a lot of the same tools that we've leveraged and built over the course of the last decade in a new way.

So, what is ORAS? Oras is a sandbox project inside the CNCF. It allows you to distribute artifacts in OCI registries. It also allows you to manage them, which means you can then manipulate the artifacts after they've been published, as well as everything you need to do to actually put them into a registry. It allows you to use it as a CLI, which the majority of our users end up using, or as part of an SDK. Um I'm actually speaking at the next right literally right after this at ArgoCon talking about how we integrated auras inside AR Argo CD to be able to then start leveraging it leveraging OCI artifacts and OCI images within Argo CD. It also has a number of of uh SDK libraries in different languages. Everything from Java, Golang, Rust, everything's out there. You really you can use it. It's also Oruras is compatible with many different popular registries inside the community. Everything from DockerHub, Quay, Zot, Harbor all are compatible with auras and many organizations have really started to adopt and implement auras inside their own tools, workflows and processes.

Now today's little quick talk is going to talk about multiplatform images. A multiplatform image means that you can distribute a single image or artifact and have it be compatible with multiple architectures. So I'm running a M1 Mac, which means I can run my the image on my machine or run it on a tradit
