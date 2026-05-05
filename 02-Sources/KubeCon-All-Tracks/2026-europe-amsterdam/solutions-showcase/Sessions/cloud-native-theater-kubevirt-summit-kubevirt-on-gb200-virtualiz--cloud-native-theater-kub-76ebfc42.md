---
type: kubecon-session
event: "KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands"
event_id: kccnceu2026
year: 2026
region: "Europe"
city: "Amsterdam"
country: "Netherlands"
event_date: "2026-03-23/2026-03-26"
track: "Solutions Showcase"
themes: ["SRE Reliability"]
speakers: ["Fan Zhang", "Kevin Klues", "and Alay Patel", "NVIDIA"]
sched_url: https://kccnceu2026.sched.com/event/2EG0e/cloud-native-theater-kubevirt-summit-kubevirt-on-gb200-virtualizing-a-rack-scale-supercomputer-fan-zhang-kevin-klues-and-alay-patel-nvidia
youtube_search_url: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+KubeVirt+Summit%3A+KubeVirt+on+GB200%3A+Virtualizing+a+Rack-Scale+Supercomputer+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Cloud Native Theater | KubeVirt Summit: KubeVirt on GB200: Virtualizing a Rack-Scale Supercomputer - Fan Zhang, Kevin Klues, and Alay Patel, NVIDIA

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Solutions Showcase]]
- Temas: [[SRE Reliability]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Fan Zhang, Kevin Klues, and Alay Patel, NVIDIA
- Schedule: https://kccnceu2026.sched.com/event/2EG0e/cloud-native-theater-kubevirt-summit-kubevirt-on-gb200-virtualizing-a-rack-scale-supercomputer-fan-zhang-kevin-klues-and-alay-patel-nvidia
- Busca YouTube: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+KubeVirt+Summit%3A+KubeVirt+on+GB200%3A+Virtualizing+a+Rack-Scale+Supercomputer+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Cloud Native Theater | KubeVirt Summit: KubeVirt on GB200: Virtualizing a Rack-Scale Supercomputer.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EG0e/cloud-native-theater-kubevirt-summit-kubevirt-on-gb200-virtualizing-a-rack-scale-supercomputer-fan-zhang-kevin-klues-and-alay-patel-nvidia
- YouTube search: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+KubeVirt+Summit%3A+KubeVirt+on+GB200%3A+Virtualizing+a+Rack-Scale+Supercomputer+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=jtnRFgu4tdI
- YouTube title: Cloud Native Theater | KubeVirt Summit: KubeVirt on GB200: Vi... Fan Zhang, Kevin Klues & Alay Patel
- Match score: 0.852
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/cloud-native-theater-kubevirt-summit-kubevirt-on-gb200-virtualizing-a/jtnRFgu4tdI.txt
- Transcript chars: 25672
- Keywords: gpu, inside, domain, compute, memory, config, virtualization, computer, single, topology, devices, workload, platform, address, demons, access, driver, configuration

### Resumo baseado na transcript

I work for the cloud native virtualization for GPU data center and AI factory. Um, and we also have Ali Patel with us today whom we're going to be swapping back a bit a bit back and forth on stage here. We can ser they can survey that the kubernetes failures p failures or covert failures. next layer the first one is a boot before we can talk about performance or topology in the gas the VM must be able to boot reliably with four GPUs and highspeed IO's attached on TP200 converter must treat 64bit MMIO aperture as the first The third is the kubernetes we are not we are not in the cumul configuration alone we are dealing with cloud native stack including scheduling cublet admission topology hints and device allocation etc. we designed a numar planner in the curver in tree codebase to align the complicated constraint for grace virtualiz ization.

### Excerpt da transcript

Hello. Hi. Um, good morning. Thanks everyone coming here. Um, my name is Fan Fan Jang. I'm from Nvidia. I work for the cloud native virtualization for GPU data center and AI factory. >> Yeah. And I'm I'm Kevin Clues. Kevin Clues. I'm also from Nvidia. Um, and we also have Ali Patel with us today whom we're going to be swapping back a bit a bit back and forth on stage here. But, um, yeah, happy to be here. >> Okay. So, I'm going to I'm going to start the first part of this talk. Uh, I'm going to share how we achieved the covert on the GB200 with a proper VM model. Um, so our goal was not just to boot a VM on GB200. Our goal was to make one covered VM behave like one computer tree. To look at the system from the left to right, we started from the GP20072 rack, then zoom in to a single computer tree and then turn that tree into a tenant VM. A typical GDX uh GB200 computer tree is a two socket system. It has two grace arm CPUs. Each CPU is conducted with two black well GPUs by the MVLink C2C. MVLink C2C is a has a 900 GB biodirectional bandwidth at the same as MVLink on GB200.

And what we wanted was very simple to say but not simple to build. One VM equals one computer tree except for passing through all the hosted devices. It has to make sure the guest see the CM NUMA and the devices locality reflecting the host. Why is that important? Because in the guest for the AI workload using CUDA niko locality is not only about performance. It affects communication behaviors, routing decisions and overall stability for token outputs. VM boundary is not just about isolation but also about prediction. So the promise we were chasing was coover provide a deterministic VM boundary on GB200 for AI factory. The twist in this story is that grace virtualization is not just passing through a larger GPU devices. GP200 is a coherent system and that changes the virtualization contract. There are three key key parts. The first one is translation on GP200 nested translation accelerated by the SMMAU is mandatory. The guest owns stage one, the host enforces stage two and M SMMEUv3 sits in the middle and the command Q helps reduce invalidation overhead on the acceler accelerated path.

The system memory used by the command Q must be contiguous. The device assignment path also relies on the OMU FD framework instead of the legacy group centric MU model. The second one is memory backing. GP200 use a cache coherent CPU toGPU interconnect. So the memory behavior matters more than on our CP
