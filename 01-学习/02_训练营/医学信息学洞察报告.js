const { Document, Packer, Paragraph, TextRun, HeadingLevel, AlignmentType, LevelFormat } = require('docx');
const fs = require('fs');

const doc = new Document({
  styles: {
    default: { document: { run: { font: "Arial", size: 24 } } },
    paragraphStyles: [
      { id: "Title", name: "Title", basedOn: "Normal",
        run: { size: 56, bold: true, color: "000000", font: "Arial" },
        paragraph: { spacing: { before: 240, after: 240 }, alignment: AlignmentType.CENTER } },
      { id: "Heading1", name: "Heading 1", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 32, bold: true, color: "000000", font: "Arial" },
        paragraph: { spacing: { before: 240, after: 180 }, outlineLevel: 0 } },
      { id: "Heading2", name: "Heading 2", basedOn: "Normal", next: "Normal", quickFormat: true,
        run: { size: 28, bold: true, color: "000000", font: "Arial" },
        paragraph: { spacing: { before: 180, after: 120 }, outlineLevel: 1 } }
    ]
  },
  numbering: {
    config: [
      { reference: "insights",
        levels: [{ level: 0, format: LevelFormat.DECIMAL, text: "%1.", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] },
      { reference: "benefits",
        levels: [{ level: 0, format: LevelFormat.BULLET, text: "•", alignment: AlignmentType.LEFT,
          style: { paragraph: { indent: { left: 720, hanging: 360 } } } }] }
    ]
  },
  sections: [{
    properties: { page: { margin: { top: 1440, right: 1440, bottom: 1440, left: 1440 } } },
    children: [
      new Paragraph({ heading: HeadingLevel.TITLE, children: [new TextRun("医学信息学洞察报告")] }),
      
      new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("一、行业背景")] }),
      new Paragraph({ spacing: { after: 200 }, children: [
        new TextRun("医学信息学是医学与信息技术的交叉学科，致力于利用信息技术改善医疗服务的质量、效率和可及性。随着大数据、人工智能、云计算等技术的快速发展，医学信息学正在经历前所未有的变革。")
      ]}),
      
      new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("二、核心洞察")] }),
      
      new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun("1. 数据驱动医疗决策")] }),
      new Paragraph({ spacing: { after: 200 }, children: [
        new TextRun("电子病历系统的普及使医疗机构积累了海量的临床数据。通过数据分析和机器学习，可以辅助医生进行疾病诊断、治疗方案选择和预后评估。例如，基于影像数据的AI诊断系统在某些疾病的识别准确率已超过人类专家。")
      ]}),
      
      new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun("2. 个性化医疗的崛起")] }),
      new Paragraph({ spacing: { after: 200 }, children: [
        new TextRun("基因组学数据与临床数据的整合为精准医疗提供了基础。通过分析患者的基因信息、生活习惯和环境因素，可以实现个性化的疾病预防和治疗方案，提高治疗效果，减少副作用。")
      ]}),
      
      new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun("3. 远程医疗加速普及")] }),
      new Paragraph({ spacing: { after: 200 }, children: [
        new TextRun("疫情推动了远程医疗的快速发展。在线问诊、远程监测、移动健康应用等模式打破了时间和空间限制，使优质医疗资源得以更广泛地覆盖。未来，5G和物联网技术将进一步提升远程医疗的体验和可靠性。")
      ]}),
      
      new Paragraph({ heading: HeadingLevel.HEADING_2, children: [new TextRun("4. 数据安全与隐私保护")] }),
      new Paragraph({ spacing: { after: 200 }, children: [
        new TextRun("医疗数据的敏感性和价值使其成为网络攻击的重点目标。在推进数字化转型的同时，必须加强数据加密、访问控制、合规监管等安全措施，平衡数据利用与隐私保护的关系。")
      ]}),
      
      new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("三、技术赋能价值")] }),
      new Paragraph({ numbering: { reference: "benefits", level: 0 }, children: [
        new TextRun("提高诊疗效率，减少误诊漏诊")
      ]}),
      new Paragraph({ numbering: { reference: "benefits", level: 0 }, children: [
        new TextRun("优化医疗资源配置，降低医疗成本")
      ]}),
      new Paragraph({ numbering: { reference: "benefits", level: 0 }, children: [
        new TextRun("促进医学研究创新，加速新药研发")
      ]}),
      new Paragraph({ numbering: { reference: "benefits", level: 0 }, spacing: { after: 200 }, children: [
        new TextRun("改善患者就医体验，提升健康素养")
      ]}),
      
      new Paragraph({ heading: HeadingLevel.HEADING_1, children: [new TextRun("四、未来展望")] }),
      new Paragraph({ spacing: { after: 200 }, children: [
        new TextRun("医学信息学将继续深度融合人工智能、区块链、边缘计算等前沿技术，构建更智能、更安全、更人性化的医疗健康生态系统。数据标准化、互操作性提升、跨学科人才培养将是未来发展的关键方向。同时，伦理法规建设也需同步推进，确保技术创新惠及每一位患者。")
      ]})
    ]
  }]
});

Packer.toBuffer(doc).then(buffer => {
  fs.writeFileSync("医学信息学洞察报告.docx", buffer);
  console.log("文档已生成：医学信息学洞察报告.docx");
});
