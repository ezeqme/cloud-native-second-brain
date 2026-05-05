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
themes: ["Storage Data"]
speakers: ["Ryosuke Tatsumi", "Hitachi America", "Ltd."]
sched_url: https://kccnceu2026.sched.com/event/2EG0h/cloud-native-theater-kubevirt-summit-achieving-10x-faster-vm-migration-to-kubevirt-with-storage-offload-in-forklift-ryosuke-tatsumi-hitachi-america-ltd
youtube_search_url: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+KubeVirt+Summit%3A+Achieving+10%C3%97+Faster+VM+Migration+to+KubeVirt+with+Storage+Offload+in+Forklift+CNCF+KubeCon+2026
slides: []
status: parsed
---

# Cloud Native Theater | KubeVirt Summit: Achieving 10× Faster VM Migration to KubeVirt with Storage Offload in Forklift - Ryosuke Tatsumi, Hitachi America, Ltd.

## Identificação

- Edição: KubeCon + CloudNativeCon Europe 2026 - Amsterdam, Netherlands
- Trilha oficial: [[Solutions Showcase]]
- Temas: [[Storage Data]]
- País/cidade: Netherlands / Amsterdam
- Speakers: Ryosuke Tatsumi, Hitachi America, Ltd.
- Schedule: https://kccnceu2026.sched.com/event/2EG0h/cloud-native-theater-kubevirt-summit-achieving-10x-faster-vm-migration-to-kubevirt-with-storage-offload-in-forklift-ryosuke-tatsumi-hitachi-america-ltd
- Busca YouTube: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+KubeVirt+Summit%3A+Achieving+10%C3%97+Faster+VM+Migration+to+KubeVirt+with+Storage+Offload+in+Forklift+CNCF+KubeCon+2026

## Resumo

Sessão da KubeCon sobre Cloud Native Theater | KubeVirt Summit: Achieving 10× Faster VM Migration to KubeVirt with Storage Offload in Forklift.

## Descrição oficial

_Descrição oficial não encontrada._

## Links

- Schedule oficial: https://kccnceu2026.sched.com/event/2EG0h/cloud-native-theater-kubevirt-summit-achieving-10x-faster-vm-migration-to-kubevirt-with-storage-offload-in-forklift-ryosuke-tatsumi-hitachi-america-ltd
- YouTube search: https://www.youtube.com/results?search_query=Cloud+Native+Theater+%7C+KubeVirt+Summit%3A+Achieving+10%C3%97+Faster+VM+Migration+to+KubeVirt+with+Storage+Offload+in+Forklift+CNCF+KubeCon+2026
## YouTube enrichment

- YouTube: https://www.youtube.com/watch?v=uRTdkZVAfWQ
- YouTube title: Cloud Native Theater | KubeVirt Summit: Achieving 10× Faster VM Migration to Kube... Ryosuke Tatsumi
- Match score: 0.882
- Transcript file: _sources/transcripts/youtube-enriched/kubecon/2026/cloud-native-theater-kubevirt-summit-achieving-10-faster-vm-migration/uRTdkZVAfWQ.txt
- Transcript chars: 13084
- Keywords: storage, migration, offload, forklift, kubevirt, target, performance, faster, bottleneck, workflow, vmware, environment, approach, operation, becomes, within, copied, host-based

### Resumo baseado na transcript

I have been working on creating storage plugin solution for Kubernetes. And today, I'd like to talk about VM migration from legacy platform to Kubevirt. However, there are technical challenges when applying this in Kubernetes environment. So, after that, I will explain our implementation architecture, including how we overcome the challenge with storage operation integration. As you know, the the Kubevirt is a powerful platform to manage virtual machine on Kubernetes. According to Gartner, uh, large-scale VM migration project can take 18 months or even longer.

### Excerpt da transcript

Hello. Uh, good afternoon. Uh, so my name is Ryosuke Tatsumi. I'm a chief researcher at Hitachi America. I have been working on creating storage plugin solution for Kubernetes. And today, I'd like to talk about VM migration from legacy platform to Kubevirt. In recent years, uh, more and more enterprise are re-evaluating their virtualization platforms. Especially with changes in the VMware ecosystem, many organizations are actively considering migration strategies. At the same time, they are not just looking for a replacement. So, they are also thinking about uh, application modernization. So, that is why platform like Kubevirt uh, gaining significant attention. So, they provide a path to run VM virtual machine today, while gradually transitioning to cloud-native architecture. However, one major challenge remains. So, how do we migrate large-scale VM environment effectively and at scale? Today, I will talk about how storage offload can solve this problem. So, this is today's agenda. First, I will start with uh, background and why VM migration throughput is becoming more important today.

Then, I will explain the key bottleneck in VM migration, especially from data transfer perspective. Next, I will introduce the storage offload approach using XCOPY. So, which changes how data is moved. However, there are technical challenges when applying this in Kubernetes environment. So, after that, I will explain our implementation architecture, including how we overcome the challenge with storage operation integration. Then, I will share performance result to show the actual impact. And finally, I will touch on our contribution to the open-source community. So, let's start with the background. As you know, the the Kubevirt is a powerful platform to manage virtual machine on Kubernetes. However, when the organization try to migrate VMs from the legacy environment, migration throughput becomes a serious bottleneck. So, this is especially critical in large enterprise environment, where they need to migrate tens of thousands of VMs and petabytes of data. So, there are two major concerns. The first one is long migration duration.

According to Gartner, uh, large-scale VM migration project can take 18 months or even longer. And this is not just a report. So, I have uh, I have also heard similar stories from people at this KubeCon. So, the where the customer uh, spend more than a year completing their migration project. The second concern is the maintenance window. The migrat
