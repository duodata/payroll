# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    "name": "Payroll",
    "version": "13.0.1.0.2",
    "category": "Human Resources",
    "website": "https://github.com/OCA/payroll",
    "sequence": 38,
    "summary": "Manage your employee payroll records",
    "license": "LGPL-3",
    "author": "Odoo SA, Odoo Community Association (OCA)",
    "depends": ["hr_contract", "hr_holidays"],
    "data": [
        "security/hr_payroll_security.xml",
        "security/ir.model.access.csv",
        "data/hr_payroll_sequence.xml",
        "data/hr_payroll_data.xml",
        "wizard/hr_payroll_contribution_register_report_views.xml",
        "wizard/hr_payroll_payslips_by_employees_views.xml",
        "views/menus.xml",
        "views/hr_contract_views.xml",
        "views/hr_contract_advantage_views.xml",
        "views/hr_payroll_structure_views.xml",
        "views/hr_salary_rule_category_views.xml",
        "views/hr_contribution_register_views.xml",
        "views/hr_salary_rule_views.xml",
        "views/hr_payslip_line_views.xml",
        "views/hr_payslip_views.xml",
        "views/hr_payslip_run_views.xml",
        "views/hr_employee_views.xml",
        "views/report_contributionregister.xml",
        "views/report_payslip.xml",
        "views/report_payslipdetails.xml",
        "report/report.xml",
        "views/res_config_settings_views.xml",
    ],
    "demo": ["demo/hr_payroll_demo.xml"],
    "application": True,
}
