---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom"
event_id: kccnceu2025
year: 2025
region: "Europe"
city: "London"
country: "United Kingdom"
event_date: "2025-04-01/2025-04-04"
track: "Emerging + Advanced"
themes: ["AI ML", "Runtime Containers"]
speakers: ["Clemens Lange", "Paul Scherrer Institute", "Valentin Volkl", "CERN"]
sched_url: https://kccnceu2025.sched.com/event/1txFV/image-snapshotters-for-efficient-container-execution-in-particle-physics-clemens-lange-paul-scherrer-institute-valentin-volkl-cern
youtube_search_url: https://www.youtube.com/results?search_query=Image+Snapshotters+for+Efficient+Container+Execution+in+Particle+Physics+CNCF+KubeCon+2025
slides: []
status: parsed
---

# Image Snapshotters for Efficient Container Execution in Particle Physics - Clemens Lange, Paul Scherrer Institute & Valentin Volkl, CERN

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2025 - London, United Kingdom
- Trilha oficial: [[Emerging + Advanced]]
- Temas: [[AI ML]], [[Runtime Containers]]
- País/cidade: United Kingdom / London
- Speakers: Clemens Lange, Paul Scherrer Institute, Valentin Volkl, CERN
- Schedule: https://kccnceu2025.sched.com/event/1txFV/image-snapshotters-for-efficient-container-execution-in-particle-physics-clemens-lange-paul-scherrer-institute-valentin-volkl-cern
- Busca YouTube: https://www.youtube.com/results?search_query=Image+Snapshotters+for+Efficient+Container+Execution+in+Particle+Physics+CNCF+KubeCon+2025

## Resumo

Sessão da KubeCon sobre Image Snapshotters for Efficient Container Execution in Particle Physics.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2025.sched.com/event/1txFV/image-snapshotters-for-efficient-container-execution-in-particle-physics-clemens-lange-paul-scherrer-institute-valentin-volkl-cern
- YouTube search: https://www.youtube.com/results?search_query=Image+Snapshotters+for+Efficient+Container+Execution+in+Particle+Physics+CNCF+KubeCon+2025
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=Dc6S4vU9GiM
- YouTube title: Image Snapshotters for Efficient Container Execution in Particle P... Clemens Lange & Valentin Volkl
- Match score: 0.894
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2025/image-snapshotters-for-efficient-container-execution-in-particle-physi/Dc6S4vU9GiM.txt
- Transcript chars: 27103
- Keywords: actually, basically, snapshot, software, pulling, download, images, container, experiments, snapshotters, registry, already, particle, experiment, instance, physics, around, efficient

### Resumo baseado na transcript

um we'll be talking about um image snapshoters in the context of particle physics where you'll see later that this actually doesn't only apply to particle physics but also beyond. Um and before we get into the details um let's briefly introduce ourselves. timeline that um you know initial collisions or operation started around 2009 right so we're now like 16 years later already and then if you look um at the end of this arrow so this is not entirely to scale here but the current plan performance is very similar as long as you're just using a lazy pulling uh snapshot and now some people might ask so what if I run on like public cloud offerings um so it's a bit difficult to get like insight into this but we found for instance that on um Google kubernetes status engine there's also an image streaming uh service and then on Microsoft Azure for instance there's they also have uh something that helps you with the image distribution and um there's also nothing that would prevent So the soi snapshot or seekable OCI uh snapshot um is actually then a fork of the star snapshot um which uh somehow addresses this problem by adding a separate index artifact to the uh to the image that is then hosted in parallel um in in the in the in the registry.

### Excerpt da transcript

um we'll be talking about um image snapshoters in the context of particle physics where you'll see later that this actually doesn't only apply to particle physics but also beyond. So I'm glad you're here. Um and before we get into the details um let's briefly introduce ourselves. I'll start with myself. So I'm a physicist. Um so I'm largely actually doing particle physics research at Paul Sher Institute PSI and um yeah I'm working on one of the experiments that is at and then again at the large collider specifically the CMS experiment and here's Valentine. Yes. So I am Valentine. I'm a physicist turned software developer and I developed a CERNVM file system that actually implements a containerd snapshot and we'll hear more about that later but first uh Clemens will introduce to you actually the problem uh that we face at CERN and why actually uh containerd snapshot solve an important problem. Great. So yeah you heard you have two physicists right in front of you. So we'll talk a bit of physics but not too much.

Um so if you think about particle physics in Switzerland um well I guess the first thing that comes to mind a lot of water um green pasture and so on. Um so actually two large um labs in Switzerland. One is the Porsche Institute or in short PSI that's Switzerland's national lab for natural sciences and engineering and then there's CERN you know widely known you've had several talks actually from CERN here at this conference the European laboratory for particle physics and they both have in common that um they're they have particle accelerators so we're basically accelerating science with accelerators and what accelerators do is in the name they accelerate particles and that means um to some extent And they um either shoot those accelerated particles then on targets or they make them collide. So um shoot them um on on each other. Right. And these um experiments or these accelerators um in principle all look very similar. So for instance there's one that's been there at PSI and since the 70s and it's been continuously upgraded the so-called ring cyclotron.

And then there's one that you've probably heard of um you know more often already. That's the certain large hydronone collider in short LHC. Okay. So when these collisions or interactions happen, there needs to be some device that actually detects these particles. Um and one of them is the CMS experiment. Um and yeah, that's the one that I'm working on. It's also a pretty uh huge uh experiment. So
