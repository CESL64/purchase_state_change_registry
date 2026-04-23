# Purchase State Change Registry

## Overview
`purchase_state_change_registry` extends the base module `state_change_registry` to provide **state tracking for purchase orders** in Odoo 18.

The module focuses on `purchase.order`, allowing purchase teams to monitor, audit, report, and notify state transitions in a structured and reusable way.

## Main Features
- 📦 Inherits `purchase.order` and monitors updates to the `state` field
- 📝 Generates a `state.change.registry` record whenever a purchase order changes state
- 💬 Posts traceability messages in the purchase order chatter
- 🔗 Relates each log with its source purchase order using `purchase_id`
- 📂 Adds a dedicated notebook page to the purchase order form
- 📄 Extends the purchase order report with state-change information
- ✉️ Implements email notification logic for purchase-related state changes
- ✅ Marks `mail_sent` after the notification flow is executed successfully
- 📅 Includes a reporting wizard filtered by date range and company

## Notification Logic
This module inherits the generic `send_state_change_notification()` hook from the base module and specializes it for purchase documents:

- only sends notifications for records where `document_type = 'purchase'`
- identifies the source document through `purchase_id`
- notifies followers of the purchase order
- keeps communication traceability in chatter

## User Interface Enhancements
- New **Registro de Cambios de Estado** tab on purchase orders
- Read-only list of related logs
- Action button per line to trigger email notifications manually
- Wizard available from the Purchase reports menu

## Reports
- 📑 Inherited QWeb section inside the purchase document report
- Adds operational context directly into the printed purchase document

## Dependencies
- `purchase`
- `state_change_registry`

## Business Value
This module supports better governance of the purchasing cycle by ensuring that every relevant state transition is:
- recorded
- reviewable
- reportable
- ready for notification workflows

It is a practical enhancement for environments where procurement control, auditability, and process transparency are important.
