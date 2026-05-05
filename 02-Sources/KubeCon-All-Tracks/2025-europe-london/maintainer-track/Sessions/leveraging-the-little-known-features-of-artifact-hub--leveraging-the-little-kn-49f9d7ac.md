---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Maintainer Track"
themes: ["AI ML", "Community Governance"]
speakers: ["Matt Farina", "SUSE"]
sched_url: https://kccnceu2025.sched.com/event/1tcyH/leveraging-the-little-known-features-of-artifact-hub-matt-farina-suse
youtube_search_url: https://www.youtube.com/results?search_query=Leveraging+the+Little+Known+Features+of+Artifact+Hub+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Leveraging the Little Known Features of Artifact Hub - Matt Farina, SUSE

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Maintainer Track]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: United Kingdom / London
- Speakers: Matt Farina, SUSE
- Schedule: https://kccnceu2025.sched.com/event/1tcyH/leveraging-the-little-known-features-of-artifact-hub-matt-farina-suse
- Busca YouTube: https://www.youtube.com/results?search_query=Leveraging+the+Little+Known+Features+of+Artifact+Hub+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Leveraging the Little Known Features of Artifact Hub.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1tcyH/leveraging-the-little-known-features-of-artifact-hub-matt-farina-suse
- YouTube search: https://www.youtube.com/results?search_query=Leveraging+the+Little+Known+Features+of+Artifact+Hub+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=HEhnch8Wpj8
- YouTube title: Leveraging the Little Known Features of Artifact Hub - Matt Farina, SUSE
- Match score: 0.94
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/leveraging-the-little-known-features-of-artifact-hub/HEhnch8Wpj8.txt
- Transcript chars: 33732
- Keywords: artifact, actually, artifacthub, artifacts, install, information, little, specify, signing, sometimes, organization, signed, metadata, security, somebody, together, provide, structure

### Resumo baseado na transcript

Thank you for coming to my talk on leveraging the little known uh features of Artifac. Um first I'll say there are a lot of slides that I'm going to go through today. So, let's walk through how do we solve some of these problems and provide more context. Software all over the place has change logs or at least changes are tracked. there's a really nice place to see it, to visualize it, to, you know, easily go back through it because sometimes going back through change logs and and commit messages isn't always the easiest. Because in the Kubernetes space, we know there's a ton of flexibility of what you can piece together with all these Lego blocks.

### Excerpt da transcript

Hello. Thank you for coming to my talk on leveraging the little known uh features of Artifac. Uh does everybody in here already know what ArtifactHub is? Anybody? Okay. So, I'm going to cover just some of this real briefly. Um first I'll say there are a lot of slides that I'm going to go through today. If you want the slides, you can go up to the scheduling system and get a copy because I'm going to breeze past some of these. I use them kind of as a backdrop for talking and I do move rather quickly. So, ArtifactHub is a CNCF incubating project now. Uh, you can get the code up on GitHub just like all of the other CNCF projects. Um, what you can run it anywhere. You can run it on your own self-hosted, but people are probably most familiar with the centralized version, right? Where you go ahead and you get all these distributed artifacts from all over the internet. This is one place to search and find them. Um, and of course, ArtifactHub, a little inception here, is actually up on ArtifactHub. You can find it, you can run it, you can install it.

Uh, you can use it yourself. So, if you want to have your own instance for, say, your own organizations's uh, artifacts to make those discoverable internally, you can absolutely do that. You could take it to your customers. You've got customers who want that. And it is something you can run yourself and find the details right up on Artifacub. That little inception helps us with that. So since the last time I talked about artifact hub, we do have one new thing that is a new type of artifact uh last uh fall at CubeCon. Um boot C joined the CNCF as a CNCF project. And so now bootable containers are an type of artifact that you can discover and work with in here alongside all of these other ones that are up there. And so that's another new artifact that's come in. The pace has slowed down a little bit because there's only so many projects that have artifacts in the CNCF in this space. And uh so that's the new one. And here I'm going to go a little deeper. If you do have questions about some of the the other stuff in here that's more higher level and basic, there was a talk that I gave at CubeCon North America last fall.

Uh you can get the video, you can get the slides, and all of that material over here. I'm going to go a little deeper into some of the other nuances, but a lot of that on the surface stuff is actually already available on the internet video form. You can find it on our blog or at this link. So, hi, I'm M
