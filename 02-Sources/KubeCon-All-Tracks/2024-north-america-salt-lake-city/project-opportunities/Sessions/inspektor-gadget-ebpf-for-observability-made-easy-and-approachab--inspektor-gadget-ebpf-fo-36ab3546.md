---
type: kubecon-session
event: "KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States"
event_id: kccncna2024
year: 2024
region: "North America"
city: "Salt Lake City"
country: "United States"
event_date: "2024-11-12/2024-11-15"
track: "Project Opportunities"
themes: ["Observability"]
speakers: []
sched_url: https://kccncna2024.sched.com/event/1iW8h/inspektor-gadget-ebpf-for-observability-made-easy-and-approachable-project-lightning-talk
youtube_search_url: https://www.youtube.com/results?search_query=Inspektor+Gadget%3A+eBPF+for+Observability%2C+Made+Easy+and+Approachable+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
slides: []
status: parsed
---

# Inspektor Gadget: eBPF for Observability, Made Easy and Approachable | Project Lightning Talk

## Identificação

- Edição: KubeCon + CloudNativeCon North America 2024 - Salt Lake City, United States
- Trilha oficial: [[Project Opportunities]]
- Temas: [[Observability]]
- País/cidade: United States / Salt Lake City
- Speakers: N/A
- Schedule: https://kccncna2024.sched.com/event/1iW8h/inspektor-gadget-ebpf-for-observability-made-easy-and-approachable-project-lightning-talk
- Busca YouTube: https://www.youtube.com/results?search_query=Inspektor+Gadget%3A+eBPF+for+Observability%2C+Made+Easy+and+Approachable+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024

## Resumo

Sessão da KubeCon sobre Inspektor Gadget: eBPF for Observability, Made Easy and Approachable | Project Lightning Talk.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccncna2024.sched.com/event/1iW8h/inspektor-gadget-ebpf-for-observability-made-easy-and-approachable-project-lightning-talk
- YouTube search: https://www.youtube.com/results?search_query=Inspektor+Gadget%3A+eBPF+for+Observability%2C+Made+Easy+and+Approachable+%7C+Project+Lightning+Talk+CNCF+KubeCon+2024
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=_nR1cHhBth8
- YouTube title: Inspektor Gadget: eBPF for Observability, Made Easy and Approachable | Project Lightning Talk
- Match score: 1.08
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2024/inspektor-gadget-ebpf-for-observability-made-easy-and-approachable-pro/_nR1cHhBth8.txt
- Transcript chars: 8245
- Keywords: ebpf, gadget, kernel, observability, inspector, program, gadgets, trace, actually, programs, similar, manager, inside, directly, security, across, containers, framework

### Resumo baseado na transcript

all right I'm just going to get it started because then I get an extra minute or two uh so yeah we're going to be talking about ebpf uh for observability and I'm going to be I'm aiming to show how it um Inspector Gadget makes it easy and approachable I'm Chris cool uh I work at Microsoft how many people have heard of ebpf okay that's a lot of hands how many people have used ebpf now have you used EF directly or have you used it through a

### Excerpt da transcript

all right I'm just going to get it started because then I get an extra minute or two uh so yeah we're going to be talking about ebpf uh for observability and I'm going to be I'm aiming to show how it um Inspector Gadget makes it easy and approachable I'm Chris cool uh I work at Microsoft how many people have heard of ebpf okay that's a lot of hands how many people have used ebpf now have you used EF directly or have you used it through a tool like psyllium or something like um Falco how many people have used it directly okay yeah so very few um we aim to change that we want you to be able to say oh I think ebpf can solve that and uh go straight to um getting that information you need so ebf we say have super has superpowers uh it allows you to tap into the kernel without modifying the kernel it runs in a sandbox and so it is guaranteed safe meaning you cannot crash the kernel uh like uh previously you could only get this kind of information through a Kel module which shared the memory um so it was unsafe it's high performant and very efficient it runs in the kernel um it uh is vent driven so you attach it to a resource in the kernel and then it um when an event happened it executes and in our case it puts that data into a ring buffer which you can pull out from the other side uh in user space it is general purpose so you hear a lot of uh networking tools or security tools or observability tools it can do those things and more and so Inspector Gadget tries to uh Prov provide you a way to use the full spectrum of of BPF for observability um so ebpf is hard uh this is why so few hands went up uh when I asked who used it directly uh so you have to first write the BPF program there's your first hurdle um are you how many how many kernel Engineers do we have in here very few about the same number as the question I asked before um first you have to write the BPF program you need that kernel knowledge uh you need to compile it to an elf um to the elf format you need to make sure it works across kernels and architectures uh you need to deploy it across your nodes uh when we're using kubernetes we need to load we need to load the EF program into the kernel uh and then that that BPF program is there it puts data in a ring buffer and then you need to gather that data from user space uh and then that data is actually raw kernel data it doesn't know anything about kubernetes or containers and so you're going to have to do some kind of mapping uh to these highle resource
