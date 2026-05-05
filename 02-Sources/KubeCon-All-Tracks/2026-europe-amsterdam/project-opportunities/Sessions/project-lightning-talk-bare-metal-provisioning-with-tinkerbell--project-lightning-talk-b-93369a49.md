---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Project Opportunities"
themes: ["AI ML", "Community Governance"]
speakers: ["Jacob Weinstock", "Maintainer"]
sched_url: https://kccnceu2026.sched.com/event/2EFxM/project-lightning-talk-bare-metal-provisioning-with-tinkerbell-jacob-weinstock-maintainer
youtube_search_url: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Bare+Metal+Provisioning+With+Tinkerbell+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Project Lightning Talk: Bare Metal Provisioning With Tinkerbell - Jacob Weinstock, Maintainer

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Project Opportunities]]
- Temas: [[AI ML]], [[Community Governance]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Jacob Weinstock, Maintainer
- Schedule: https://kccnceu2026.sched.com/event/2EFxM/project-lightning-talk-bare-metal-provisioning-with-tinkerbell-jacob-weinstock-maintainer
- Busca YouTube: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Bare+Metal+Provisioning+With+Tinkerbell+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Project Lightning Talk: Bare Metal Provisioning With Tinkerbell.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EFxM/project-lightning-talk-bare-metal-provisioning-with-tinkerbell-jacob-weinstock-maintainer
- YouTube search: https://www.youtube.com/results?search_query=Project+Lightning+Talk%3A+Bare+Metal+Provisioning+With+Tinkerbell+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=DvsMNlrOxcM
- YouTube title: Project Lightning Talk: Bare Metal Provisioning With Tinkerbell - Jacob Weinstock, Maintainer
- Match score: 0.901
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/project-lightning-talk-bare-metal-provisioning-with-tinkerbell/DvsMNlrOxcM.txt
- Transcript chars: 4474
- Keywords: tinkerbell, hardware, provisioning, allows, template, native, define, operating, machines, physical, hopefully, little, provision, nature, called, install, github, object

### Resumo baseado na transcript

So, uh, Tinkerbell's a a little bit of a different way in which we can provision physical hardware. Um, if you're familiar with some of the older technologies, Kickstart, um, or pixie booting, things of that nature. We also have solved um a potential problem with uh how do you provision hardware without provisioning your provisioning stack, right? So not only can Tinkerbell do um arbitrary operating system installs, but we can do full Kubernetes installations through our uh cap t provider. Um come find us, look it up in the schedule, and then on on Wednesday, we'll have a project booth where you can come and we can talk and we can give demos and you can see all about it.

### Excerpt da transcript

My name is Jacob Weintock. I'm the core maintainer of the Tinkerbell project. Um, we are a Kubernetes native bare metal provisioning engine. How many folks out here have onrem physical hardware? They nice. How many How many home labers? Oh, nice. Maybe even more. I like it. Hopefully Tinkerbell can be a part of your uh your systems there. What is Tinkerbell? So, uh, Tinkerbell's a a little bit of a different way in which we can provision physical hardware. Um, if you're familiar with some of the older technologies, Kickstart, um, or pixie booting, things of that nature. Tinkerbell goes about it in a little different way. We're Kubernetes native. So, we have uh, CRDs for all the things. U, we have hardware CRD, which allows you to just define your disc, your network, all the things about your hardware. And then we have what's called a template. Inside of there, you define how you install your operating system. And when you dive in, you'll see the template looks very similar to what you might have with um any kind of CI system.

So, GitHub actions or uh build kite, etc. Right? This is a manifest that allows you to lay out disk images, do partitioning, updates files on disk, do things of that nature. And then when you combine those two, a hardware and a template object, uh we get what we call a workflow. And that allows you to do power operations. You can reboot. You can uh pixie boot. You can do uh ISO mounting. So you can do full layer three static provisioning. Um run your installation, reboot, kc, do whatever next steps you need to do. Um and all of this comes in like I said in a very Kubernetes native way. Um some of the features that we've recently landed in our projects um include a readonly web UI. Um, we have a new lightweight in-memory operating system called Hook OS, which is the successor to, excuse me, we have Captain OS, which is the successor to Hook OS. Um, all things Peter Pan related as you can see with our naming schemas here. Uh, we have a serial over SSH that allows you to SSH through Tinkerbell into the console of your BMC using public keys.

No more needing to play with IPMI tool and make sure you have all that set up properly. Uh we also have some discovery modes. So you can plug Tink you can set up Tinkerbell, install it and without actually having to define any of the previous CRDs we talked about, you could turn your machines on. Tinkerbell will autodiscocover all those machines, create CRDs for you and even run workflows uh based o
